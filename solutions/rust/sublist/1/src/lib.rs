#[derive(Debug, PartialEq, Eq)]
pub enum Comparison {
    Equal,
    Sublist,
    Superlist,
    Unequal,
}

fn is_superlist<T: PartialEq>(a: &[T], b: &[T]) -> bool {
    if a.is_empty() & !b.is_empty() {
        return false;
    } else if !a.is_empty() & b.is_empty() {
        return true;
    }

    a.windows(b.len()).any(|window| window == b)
}

pub fn sublist<T: PartialEq>(_first_list: &[T], _second_list: &[T]) -> Comparison {
    if _first_list == _second_list {
        Comparison::Equal
    } else if is_superlist(_first_list, _second_list) {
        Comparison::Superlist
    } else if is_superlist(_second_list, _first_list) {
        Comparison::Sublist
    } else {
        Comparison::Unequal
    }
}
