from models.schemas import TripRequest
from agents.trip_planner_agent import get_trip_planner_agent  # 这里改成你的文件名

# 1. 创建请求
req = TripRequest(
    city="上海",
    start_date="2025-10-01",
    end_date="2025-10-03",
    travel_days=3,
    preferences=["景点", "美食"],
    transportation="公共交通",
    accommodation="舒适型"
)

# 2. 获取 planner
planner = get_trip_planner_agent()

# 3. 执行规划
plan = planner.plan_trip(req)


# 4. 输出结果
print(plan)