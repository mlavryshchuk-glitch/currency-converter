# currency-converter
Currency converter (UAH -> USD/EUR)

| Error Type | Trigger | Resulting Message |
| --- | --- | --- |
| **ValueError** | User enters text instead of a number or a negative value. | "Amount input Error: please check if you entered a valid number." |
| **KeyError** | User enters a currency not in the `RATES` dictionary (e.g., "GBP"). | "Currency selection Error: please choose a supported currency." |

### 3. Input Validation

The code includes a manual check for negative numbers:

```python
if uah_amount < 0:
    raise ValueError("The amount cannot be negative.")

```

---

## 🚀 Example Usage

**Successful Conversion:**

```text
Welcome to the Currency Converter (UAH -> EUR/USD)!
Enter the amount in UAH: 1000
Enter the target currency (EUR/USD): usd
1000.0 UAH is equal to 27.00 USD.

```

**Handling an Error:**

```text
Enter the amount in UAH: 1000
Enter the target currency (EUR/USD): GBP
Currency selection Error: please choose a supported currency (EUR or USD).

```




