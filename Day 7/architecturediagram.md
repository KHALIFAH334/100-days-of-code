graph TB
    %% External Layer
    User((Clinicians / Users))
    
    Edge Layer
    subgraph Edge [Public Edge Layer]
        R53[Route 53 DNS]
        WAF[AWS WAF]
        CF[CloudFront]
        S3_Static[S3: Frontend Assets]
    end

     VPC Layer
    subgraph VPC [VPC - Multi-AZ / No Direct Inbound Access]
        
        subgraph Public_Subnets [Public Subnets]
            ALB_Pub[Public ALB - HTTPS]
            NAT[NAT Gateways]
        end
        
        subgraph Private_Compute [Private Compute Subnets]
            ALB_Priv[Private ALB - Internal Routing]
            
            subgraph ECS [ECS Fargate Cluster]
                WEB[platform-web]
                API[platform-api]
                CWS[clinical-workflow-service]
                AI[ai-service]
            end
        end
        
        subgraph Private_Data [Private Data Subnets]
            RDS[(RDS PostgreSQL - Multi-AZ)]
            Redis[(ElastiCache Redis)]
        end
    end

    AWS Managed Services Layer
    subgraph AWS_Managed [Security & Observability]
        Secrets[AWS Secrets Manager]
        S3_Docs[S3: Clinical Docs - Encrypted]
        S3_Audit[S3: Audit Logs - Object Lock]
        CW[CloudWatch & X-Ray]
    end

     Traffic Flow
    User --> R53
    R53 --> WAF
    WAF --> CF
    CF --> S3_Static
    WAF --> ALB_Pub
    
    ALB_Pub --> WEB
    ALB_Pub --> API
    ALB_Pub --> ALB_Priv
    
    ALB_Priv --> CWS
    ALB_Priv --> AI
    
    %% Compute to Data Flow
    WEB --> Redis
    API --> RDS
    API --> Redis
    CWS --> RDS
    CWS --> Redis
    AI -.-> CW
    
    %% Outbound & Managed Services Flow
    ECS -.-> NAT
    ECS -.-> Secrets
    API -.-> S3_Docs
    CWS -.-> S3_Docs
    ECS -.-> CW