select machine_id,
Round(
    sum(
        case 
            when activity_type = 'start' then -timestamp
                else timestamp
            end)/(count(*)/2),3) as processing_time
from  Activity
group by machine_id