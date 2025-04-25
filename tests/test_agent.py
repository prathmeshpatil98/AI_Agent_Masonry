

import pytest
from research_agent import research_agent


@pytest.mark.parametrize("query", [
    "Latest trends in AI technology and What is AI Agent ?",
    "Impact of AI on education",
    "Top programming languages in 2025"
])
def test_research_agent_runs(query):
    """Test if the agent returns a non-empty summary for different queries."""
    result = research_agent(query)
    assert isinstance(result, str)
    assert len(result) > 100  
