# Project 1: Automated Inventory Auditor 

### The Business Problem
Small businesses often lose revenue because they cannot track expiring stock manually. This script solves that "Ground Reality" crisis.

### How it Works
This Python script uses **Pandas** to:
* Filter items with stock < 5.
* Identify items expiring within 30 days.
* Generate an instant **Priority Action List** (.csv).

### Script and Solution Philosophy
*Automating the robotic tasks to restore human juice to local businesses.*

---

## 🌟 New Feature: Gold Price Auditor (`gold_auditor.py`)
I added this tool to help people verify jewelry prices.

**What it does:**
* Calculates the "Fair Market Price" based on current 22K rates.
* Factors in the 3% GST and HUID charges.
* **The Logic:** It reveals the hidden "Making Charges" and tells you if you are getting a fair deal or being overcharged.

**How to use it:**
Run `python gold_auditor.py` and enter the weight and price from your jewelry quote.