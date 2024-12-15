import scala.collection.mutable
import scala.util.boundary
import scala.util.boundary.break

/**
 * Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
 * In other words, return true if one of s1's permutations is the substring of s2.
 */
def permutation_as_substring(s1: String, s2: String): Boolean =
  val frequency = mutable.HashMap[Char, Int]().withDefaultValue(0)
  for (c <- s1) do
    frequency(c) += 1

  var l = 0
  while l < s2.length && !frequency.contains(s2(l)) do l += 1

  var r = l
  boundary:
    while r < s2.length && l < s2.length && l <= r do
      if frequency(s2(r)) > 0 then
        frequency(s2(r)) -= 1
        r += 1
      else
        frequency(s2(l)) += 1
        l += 1
      if frequency.values.sum == 0 then break(true)
    false
