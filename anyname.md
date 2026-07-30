```mermaid
gantt
    title Anchorcapital Project Timeline (14 Weeks)
    dateFormat  YYYY-MM-DD
    tickInterval 1w
    
    section Design
    Chapters 1-3, Lit Review & Architecture :a1, 2026-08-03, 14d
    
    section Smart Contracts
    Smart Contract Dev (Anchor, Rust) & Token-2022 :a2, after a1, 21d
    
    section Backend
    Database Setup (Supabase) & API Routing :a3, after a2, 14d
    
    section Frontend
    Frontend UI/UX (Next.js) & Web3 Integration :a4, after a3, 21d
    
    section Testing
    System Integration & Security Testing :a5, after a4, 14d
    
    section Finalization
    Final Documentation, Reporting & Defense :a6, after a5, 14d