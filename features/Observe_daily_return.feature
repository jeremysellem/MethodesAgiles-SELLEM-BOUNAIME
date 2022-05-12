Feature: un trader partage son "daily yield" au trader chef


  Scenario Outline: give Daily Yield
   Given Un TraderChef et son daily <current_daily>
    When Un trader performe son <new_daily> et le transmet à son trader chef
    Then Le trader chef peut observer le <updated_daily> de son trader
    Examples:
    |current_daily | new_daily | updated_daily |
    | 4            | 3         | 7             |
    | 7.1          | 5.2       | 12.3          |
    | -1           | 4         | 3             |