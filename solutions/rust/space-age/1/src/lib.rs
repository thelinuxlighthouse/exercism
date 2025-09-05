// The code below is a stub. Just enough to satisfy the compiler.
// In order to pass the tests you can add-to or change any of this code.

const EARTH_SECONDS: f64 = 31557600.0;
#[derive(Debug)]
pub struct Duration(f64);

impl From<u64> for Duration {
    fn from(s: u64) -> Self {
        Self(s as f64)
    }
}

pub trait Planet {
    fn years_during(d: &Duration) -> f64 {
        todo!("convert a duration ({d:?}) to the number of years on this planet for that duration");
    }
}

pub struct Mercury;
pub struct Venus;
pub struct Earth;
pub struct Mars;
pub struct Jupiter;
pub struct Saturn;
pub struct Uranus;
pub struct Neptune;

impl Planet for Mercury {
    fn years_during(d: &Duration) -> f64 {
        ((d.0 / (EARTH_SECONDS * 0.2408467)) * 100.0).round() / 100.0
    }
}
impl Planet for Venus {
    fn years_during(d: &Duration) -> f64 {
        ((d.0 / (EARTH_SECONDS * 0.61519726)) * 100.0).round() / 100.0
    }
}
impl Planet for Earth {
    fn years_during(d: &Duration) -> f64 {
        ((d.0 / EARTH_SECONDS) * 100.0).round() / 100.0
    }
}
impl Planet for Mars {
    fn years_during(d: &Duration) -> f64 {
        ((d.0 / (EARTH_SECONDS * 1.8808158)) * 100.0).round() / 100.0
    }
}
impl Planet for Jupiter {
    fn years_during(d: &Duration) -> f64 {
        ((d.0 / (EARTH_SECONDS * 11.862615)) * 100.0).round() / 100.0
    }
}
impl Planet for Saturn {
    fn years_during(d: &Duration) -> f64 {
        ((d.0 / (EARTH_SECONDS * 29.447498)) * 100.0).round() / 100.0
    }
}
impl Planet for Uranus {
    fn years_during(d: &Duration) -> f64 {
        ((d.0 / (EARTH_SECONDS * 84.016846)) * 100.0).round() / 100.0
    }
}
impl Planet for Neptune {
    fn years_during(d: &Duration) -> f64 {
        ((d.0 / (EARTH_SECONDS * 164.79132)) * 100.0).round() / 100.0
    }
}
