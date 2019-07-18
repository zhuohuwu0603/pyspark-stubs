# Stubs for pyspark.sql.functions (Python 3.5)

from typing import overload
from typing import Any, Optional, Union, Dict, Callable

import pandas.core.frame   # type: ignore
import pandas.core.series     # type: ignore

from pyspark.sql._typing import ColumnOrName
from pyspark.sql.column import Column
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.types import DataType, StructField

def approxCountDistinct(col: ColumnOrName, rsd: Optional[float] = ...) -> Column: ...
def approx_count_distinct(col: Column, rsd: Optional[float] = ...) -> Column: ...
def broadcast(df: DataFrame) -> DataFrame: ...
def coalesce(*cols: ColumnOrName) -> Column: ...
def corr(col1: ColumnOrName, col2: ColumnOrName) -> Column: ...
def covar_pop(col1: ColumnOrName, col2: ColumnOrName) -> Column: ...
def covar_samp(col1: ColumnOrName, col2: ColumnOrName) -> Column: ...
def countDistinct(col: ColumnOrName, *cols: ColumnOrName) -> Column: ...
def first(col: ColumnOrName, ignorenulls: bool = ...) -> Column: ...
def grouping(col: ColumnOrName) -> Column: ...
def grouping_id(*cols: ColumnOrName) -> Column: ...
def input_file_name() -> Column: ...
def isnan(col: ColumnOrName) -> Column: ...
def isnull(col: ColumnOrName) -> Column: ...
def last(col: ColumnOrName, ignorenulls: bool = ...) -> Column: ...
def monotonically_increasing_id() -> Column: ...
def nanvl(col1: ColumnOrName, col2: ColumnOrName) -> Column: ...
def rand(seed: Optional[int] = ...) -> Column: ...
def randn(seed: Optional[int] = ...) -> Column: ...
def round(col: ColumnOrName, scale: int = ...) -> Column: ...
def bround(col: ColumnOrName, scale: int = ...) -> Column: ...
def shiftLeft(col: ColumnOrName, numBits: int) -> Column: ...
def shiftRight(col: ColumnOrName, numBits: int) -> Column: ...
def shiftRightUnsigned(col, numBits) -> Column: ...
def spark_partition_id() -> Column: ...
def expr(str: str) -> Column: ...
def struct(*cols: ColumnOrName) -> Column: ...
def greatest(*cols: ColumnOrName) -> Column: ...
def least(*cols: Column) -> Column: ...
def when(condition: Column, value) -> Column: ...
@overload
def log(arg1: ColumnOrName) -> Column: ...
@overload
def log(arg1: float, arg2: ColumnOrName) -> Column: ...
def log2(col: ColumnOrName) -> Column: ...
def conv(col: ColumnOrName, fromBase: int, toBase: int) -> Column: ...
def factorial(col: ColumnOrName) -> Column: ...
def lag(col: ColumnOrName, count: int = ..., default: Optional[Any] = ...) -> Column: ...
def lead(col: ColumnOrName, count: int = ..., default: Optional[Any] = ...) -> Column: ...
def ntile(n: int) -> Column: ...
def current_date() -> Column: ...
def current_timestamp() -> Column: ...
def date_format(date: ColumnOrName, format: str) -> Column: ...
def year(col: ColumnOrName) -> Column: ...
def quarter(col: ColumnOrName) -> Column: ...
def month(col: ColumnOrName) -> Column: ...
def dayofmonth(col: ColumnOrName) -> Column: ...
def dayofyear(col: ColumnOrName) -> Column: ...
def hour(col: ColumnOrName) -> Column: ...
def minute(col: ColumnOrName) -> Column: ...
def second(col: ColumnOrName) -> Column: ...
def weekofyear(col: ColumnOrName) -> Column: ...
def date_add(start: ColumnOrName, days: int) -> Column: ...
def date_sub(start: ColumnOrName, days: int) -> Column: ...
def datediff(end: ColumnOrName, start: ColumnOrName) -> Column: ...
def add_months(start: ColumnOrName, months: int) ->  Column: ...
def months_between(date1: ColumnOrName, date2: ColumnOrName) -> Column: ...
def to_date(col: ColumnOrName, format: Optional[str]) -> Column: ...
@overload
def to_timestamp(col: ColumnOrName) -> Column: ...
@overload
def to_timestamp(col: ColumnOrName, format: str) -> Column: ...
def trunc(date: ColumnOrName, format: str) -> Column: ...
def next_day(date: ColumnOrName, dayOfWeek: str) -> Column: ...
def last_day(date: ColumnOrName) -> Column: ...
def from_unixtime(timestamp: ColumnOrName, format: str = ...) -> Column: ...
def unix_timestamp(timestamp: Optional[ColumnOrName] = ..., format: str = ...) -> Column: ...
def from_utc_timestamp(timestamp: ColumnOrName, tz: str) -> Column: ...
def to_utc_timestamp(timestamp: ColumnOrName, tz: str) -> Column: ...
def window(timeColumn: ColumnOrName, windowDuration: str, slideDuration: Optional[str] = ..., startTime: Optional[str] = ...) -> Column: ...
def crc32(col: ColumnOrName) -> Column: ...
def md5(col: ColumnOrName) -> Column: ...
def sha1(col: ColumnOrName) -> Column: ...
def sha2(col: ColumnOrName, numBits: int) -> Column: ...
def hash(*cols: ColumnOrName) -> Column: ...
def concat(*cols: ColumnOrName) -> Column: ...
def concat_ws(sep: str, *cols: ColumnOrName) -> Column: ...
def decode(col: ColumnOrName, charset: str) -> Column: ...
def encode(col: ColumnOrName, charset: str) -> Column: ...
def format_number(col: ColumnOrName, d: str) -> Column: ...
def format_string(format: str, *cols: ColumnOrName) -> Column: ...
def instr(str: ColumnOrName, substr: str) -> Column: ...
def substring(str: ColumnOrName, pos: int, len: int) -> Column: ...
def substring_index(str: ColumnOrName, delim: str, count: int) -> Column: ...
def levenshtein(left: ColumnOrName, right: ColumnOrName) -> Column: ...
def locate(substr: str, str: Column, pos: int = ...) -> Column: ...
def lpad(col: Column, len: int, pad: str) -> Column: ...
def rpad(col: Column, len: int, pad: str) -> Column: ...
def repeat(col: Column, n: int) -> Column: ...
def split(str: Column, pattern: str) -> Column: ...
def regexp_extract(str: ColumnOrName, pattern: str, idx: int) -> Column: ...
def regexp_replace(str: ColumnOrName, pattern: str, replacement: str) -> Column: ...
def initcap(col: ColumnOrName) -> Column: ...
def soundex(col: ColumnOrName) -> Column: ...
def bin(col: ColumnOrName) -> Column: ...
def hex(col: ColumnOrName) -> Column: ...
def unhex(col: ColumnOrName) -> Column: ...
def length(col: ColumnOrName) -> Column: ...
def translate(srcCol: ColumnOrName, matching: str, replace: str) -> Column: ...
def create_map(*cols: ColumnOrName) -> Column: ...
def array(*cols: ColumnOrName) -> Column: ...
def array_contains(col: ColumnOrName, value: Any) -> Column: ...
def explode(col: ColumnOrName) -> Column: ...
def posexplode(col: ColumnOrName) -> Column: ...
def get_json_object(col: ColumnOrName, path: str) -> Column: ...
def json_tuple(col: ColumnOrName, *fields: str) -> Column: ...
def from_json(col: ColumnOrName, schema: StructField, options: Dict[str, str] = ...) -> Column: ...
def to_json(col: ColumnOrName, options: Dict[str, str] = ...) -> Column: ...
def size(col: ColumnOrName) -> Column: ...
def sort_array(col: ColumnOrName, asc: bool = ...) -> Column: ...

class UserDefinedFunction:
    func = ...  # type: Callable[..., Any]
    returnType = ...  # type: DataType
    def __init__(self, func: Callable[..., Any], returnType: DataType, name: Optional[str] = ...) -> None: ...
    def __call__(self, *cols: ColumnOrName) -> Column: ...

def udf(f: Callable[..., Any], returnType: DataType = ...) -> Callable[..., Column]: ...

def abs(col: Column) -> Column: ...
def acos(col: ColumnOrName) -> Column: ...
def asc(col: ColumnOrName) -> Column: ...
def ascii(col: Column) -> Column: ...
def asin(col: ColumnOrName) -> Column: ...
def atan(col: ColumnOrName) -> Column: ...
def atan2(col: ColumnOrName) -> Column: ...
def avg(col: ColumnOrName) -> Column: ...
def base64(col: Column) -> Column: ...
def bitwiseNOT(col: Column) -> Column: ...
def cbrt(col: ColumnOrName) -> Column: ...
def ceil(col: ColumnOrName) -> Column: ...
def col(col: str) -> Column: ...
def collect_list(col: ColumnOrName) -> Column: ...
def collect_set(col: ColumnOrName) -> Column: ...
def column(col: str) -> Column: ...
def cos(col: ColumnOrName) -> Column: ...
def cosh(col: ColumnOrName) -> Column: ...
def count(col: ColumnOrName) -> Column: ...
def cume_dist() -> Column: ...
def degrees(col: ColumnOrName) -> Column: ...
def dense_rank() -> Column: ...
def desc(col: ColumnOrName) -> Column: ...
def exp(col: ColumnOrName) -> Column: ...
def expm1(col: ColumnOrName) -> Column: ...
def floor(col: ColumnOrName) -> Column: ...
def hypot(col: ColumnOrName) -> Column: ...
def kurtosis(col: ColumnOrName) -> Column: ...
def lit(col: Any) -> Column: ...
def log10(col: ColumnOrName) -> Column: ...
def log1p(col: ColumnOrName) -> Column: ...
def lower(col: Column) -> Column: ...
def ltrim(col: Column) -> Column: ...
def max(col: ColumnOrName) -> Column: ...
def mean(col: ColumnOrName) -> Column: ...
def min(col: ColumnOrName) -> Column: ...
def percent_rank() -> Column: ...
def pow(col1: ColumnOrName, col2: ColumnOrName) -> Column: ...
def radians(col: ColumnOrName) -> Column: ...
def rank() -> Column: ...
def reverse(col: ColumnOrName) -> Column: ...
def rint(col: ColumnOrName) -> Column: ...
def row_number() -> Column: ...
def rtrim(col: Column) -> Column: ...
def signum(col: ColumnOrName) -> Column: ...
def sin(col: ColumnOrName) -> Column: ...
def sinh(col: ColumnOrName) -> Column: ...
def skewness(col: ColumnOrName) -> Column: ...
def sqrt(col: ColumnOrName) -> Column: ...
def stddev(col: ColumnOrName) -> Column: ...
def stddev_pop(col: ColumnOrName) -> Column: ...
def stddev_samp(col: ColumnOrName) -> Column: ...
def sum(col: ColumnOrName) -> Column: ...
def sumDistinct(col: ColumnOrName) -> Column: ...
def tan(col: ColumnOrName) -> Column: ...
def tanh(col: ColumnOrName) -> Column: ...
def toDegrees(col: ColumnOrName) -> Column: ...
def toRadians(col: ColumnOrName) -> Column: ...
def trim(col: ColumnOrName) -> Column: ...
def unbase64(col: Column) -> Column: ...
def upper(col: Column) -> Column: ...
def var_pop(col: ColumnOrName) -> Column: ...
def var_samp(col: ColumnOrName) -> Column: ...
def variance(col: ColumnOrName) -> Column: ...

def dayofweek(col: ColumnOrName) -> Column: ...
def date_trunc(format: str, timestamp: ColumnOrName) -> Column: ...
def explode_outer(col: ColumnOrName) -> Column:  ...
def posexplode_outer(col: ColumnOrName) -> Column: ...
def map_keys(col :ColumnOrName) -> Column: ...
def map_values(col: ColumnOrName) -> Column: ...

class PandasUDFType:
    SCALAR: int = ...
    GROUPED_MAP: int = ...

@overload
def pandas_udf(f: Callable[..., pandas.core.series.Series], returnType: StructField, functionType: int) -> Callable[..., Column]: ...
@overload
def pandas_udf(f: Callable[[pandas.core.frame.DataFrame], pandas.core.frame.DataFrame], returnType: StructField, functionType: int) -> Callable[..., Column]: ...  # type: ignore
