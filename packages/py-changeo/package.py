# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyChangeo(PythonPackage):
    """A bioinformatics toolkit for processing high-throughput lymphocyte receptor sequencing data."""

    homepage = "http://changeo.readthedocs.io"
    pypi = "changeo/changeo-1.3.0.tar.gz"

    version(
        "0.3.0",
        sha256="7d51ef30b6e9946371160293d350569d8b54abb87c422a84251fa9c83b5664fe",
    )
    version(
        "0.3.1",
        sha256="f1d4e7a93419cb2888dcda50680632b9ce40ba5772a4b90b5885d5c0597094e6",
    )
    version(
        "0.3.10",
        sha256="a247605dba8745daae448c5b29ca2ab238a56a5cbff76af65ad44b880c10e7c5",
    )
    version(
        "0.3.11",
        sha256="4f8fd2e26c34b5ca524f4403705feb1686c7a5771e406daf17f0fa5e28a8f847",
    )
    version(
        "0.3.12",
        sha256="bffedb456141a68c063dcee39ae1837c33a1db186bb0ddc73198c392c18b34ae",
    )
    version(
        "0.3.2",
        sha256="03a604aa90b537f596452300fb73a12dad6210f7b8d929dc1b76c7b57e10b9be",
    )
    version(
        "0.3.3",
        sha256="fc43300c5257d2fb2d97d9f9e1fac00fffceab698d5b61e0969b43a6a78a9bdc",
    )
    version(
        "0.3.4",
        sha256="5886243490785470eee50f0439e4c43e14615b574284ef875cf9f32c051b8070",
    )
    version(
        "0.3.5",
        sha256="7ec084a3496663da0ba4bd4e925b4af64e78829f8e0a07968bd9ca225cfb82e7",
    )
    version(
        "0.3.6",
        sha256="a33fa47f7bbfc9400b7ba90c4fedf3ee589481b241895c5e269da8381f3b9735",
    )
    version(
        "0.3.7",
        sha256="c172b52cef49076dbbfc35003e35cfed34f643020736ef18face8727be25016c",
    )
    version(
        "0.3.8",
        sha256="0b597a232ee8f257323905168c5ad92bf25118d825f2268d9cbfcb92873efa48",
    )
    version(
        "0.3.9",
        sha256="bdcf8d97050338021b64d996d206aa743232bca3d6e85a96db563bef2cc85c8a",
    )
    version(
        "0.4.1",
        sha256="abf52174106c41caa3441cb24e9b9fc2472638194cc847d08e628c3a280c0218",
    )
    version(
        "0.4.2",
        sha256="f3916a65b50fef3666a2eb0052ddf8dcb331ff51098a2da7495b2546065eaee3",
    )
    version(
        "0.4.3",
        sha256="e7972ed9333731ed390024b51ff5bf9f175d0a802471c28376fe2b9fe8241a6b",
    )
    version(
        "0.4.4",
        sha256="7d19ac3873acf83abe6115b7f4787629a622b0fc3095e8a3ab4b35a675d163e2",
    )
    version(
        "0.4.5",
        sha256="ace48d97f0675eeb0f8bd8cd5d2bfd627ae81dd7caf1fc368f90c62e8783ea6a",
    )
    version(
        "0.4.6",
        sha256="ac5c4c3fb916e0d10e5b3b58877105b1be634c00795e2fb5acdbaca5b3f487e8",
    )
    version(
        "1.0.0",
        sha256="fb576c1775dbfee314272fb61e0935f60163796e81257eabf682d8eda4cd71bb",
    )
    version(
        "1.0.1",
        sha256="0876e3d5985b83446dd99eea5187ef6f551e6021be59046ef2431ffa3166b904",
    )
    version(
        "1.0.2",
        sha256="ee3b3f85e8fcb353d07d2a3977f77a11f0b5382dc9fd97faca6891ab8793f7fa",
    )
    version(
        "1.1.0",
        sha256="bf2c115b5199c3283ae0848e2a4f6be46b50e36a1d1584b8f7506381e74d1cb6",
    )
    version(
        "1.2.0",
        sha256="5ce34df6065804e0a8794f8d5dee6df6624496f9f9c75da821276092fe84590e",
    )
    version(
        "1.3.0",
        sha256="febec2503086b4d76a177d60f9bcb742645d24417750e976409790e9b68288ad",
    )

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-presto", type=("build", "run"))
