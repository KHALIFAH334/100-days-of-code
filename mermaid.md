flowchart TD
    A[Frontend<br/>(Next.js UI)] --> K[Compliance & KYC<br/>(identity verification)]
    A --> C[User Experience<br/>(accessibility)]
    B[Solana Token-2022 & PDAs] --> D[Custody & Control<br/>(secure escrow, dividend management)]
    B --> E[RWA Tokens / Fee Logic<br/>(on-chain dividend settings)]
    C[Anchor / Rust Programs] --> D
    C --> F[Solana Security Model<br/>(tailored auditing)]
    G[Off-chain Batching & Verifiable Computation] --> H[High Fee Barrier<br/>(reduces txn count)]
    G --> I[Auditability Gap<br/>(on-chain commitments)]
    J[Multi-sig/TSS & Distributed Key Control] --> D
    J --> L[Centralization Risk<br/>(avoids single point of control)]
    K[KYC/AML Middleware] --> K
    K --> M[Regulatory Compliance<br/>(integrated checks)]
    N[Supabase Backend] --> K
    N --> D