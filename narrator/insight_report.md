# Capstone Project Liya: Executive Insight Report

## 1. Executive Summary
This report summarizes the end-to-end data analytics findings for the Liya e-commerce dataset. Following data cleaning, deduplication, and outlier treatment, the total reconciled revenue stands at **₹97,358.30**.

## 2. Data Hygiene & Revenue Reconciliation
- **Raw Total Revenue:** ₹99,860.20
- **Cleaned Total Revenue:** ₹97,358.30
- **Delta:** ₹2,501.90 exactly accounted for by removing 5 duplicate order rows.

## 3. Key Risk Factors (Payment Methods & City Tiers)
- **COD Return Rate:** 44.4%, which is more than 3x higher than prepaid card transactions (14.7%).
- **High-Risk Segment:** Tier 2 cities utilizing Cash on Delivery face severe return exposure peaking at 54.5%.

## 4. Outlier Analysis & Time-Series Impact
Bulk order anomalies (such as quantities of 25 and 30) heavily distorted January 2026 performance figures, inflating apparent monthly revenue to ₹29,582.10 before correcting down to a true baseline of ₹11,637.10.

## 5. Strategic Recommendations
1. Incentivize prepaid checkout options (UPI/Card) to mitigate the 44.4% COD return liability.
2. Implement strict order verification rules for bulk quantity purchases in Tier 2 cities.
