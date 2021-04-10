from auroraledger.core import sample_daybook
from auroraledger.insights import domain_totals, render_daybook
from auroraledger.store import DaybookStore


def test_domain_totals_split_across_domains() -> None:
    entries = sample_daybook()
    totals = domain_totals(entries)
    assert totals.get("web2", 0) > 0
    assert totals.get("web3", 0) > 0


def test_store_filters_and_tags() -> None:
    store = DaybookStore.from_sample()
    web3_entries = store.filter_by_domain("web3")
    assert all(entry.domain == "web3" for entry in web3_entries)
    assert store.total_minutes("web3") == sum(entry.effort_minutes for entry in web3_entries)
    assert "wallet" in store.tags_for_domain("web3")


def test_render_daybook_contains_summary_block() -> None:
    rendered = render_daybook(sample_daybook())
    assert "Summary" in rendered
