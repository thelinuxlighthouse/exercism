const GIGA_SECOND: f32 = 1000000000.0;

use time::PrimitiveDateTime as DateTime;

// Returns a DateTime one billion seconds after start.
pub fn after(start: DateTime) -> DateTime {
    start + time::Duration::seconds_f32(GIGA_SECOND)
}
