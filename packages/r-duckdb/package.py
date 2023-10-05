# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RDuckdb(RPackage):
    """The DuckDB project is an embedded analytical data management system with support for the Structured Query Language (SQL)."""

    homepage = "https://duckdb.org/"
    cran = "duckdb"

    version("0.8.1-3", sha256="ee797342ea9307cf140c5d701b19ab24f08fc1339fadeb631279b771a7c6f75e")
    version("0.8.1-2", sha256="14731b4dc5f78aee9e9fea43a6ec970071646c7d66d8d0cbbd6ef93d1c1ac76a")
    version("0.8.1-1", sha256="e2e88c66ee0c9c0d89e7d4c6785bbae660e770c958325ed9d7e4092fe4f3d50b")
    version("0.8.1", sha256="a2d249cb6ca5ce8239c066ed302fa370dee534cae4508a18835c8e90f29d1e5a")
    version("0.8.0", sha256="b4f73ab2c8739d43cc8521120ec7144c3c432a2b284e874f0ed1b58326c97648")
    version("0.7.1-1", sha256="c2cf7f7b3a598a0bc19cd9c2c5361cd1766b51bebd5f3d227adf0d733db71ca6")
    version("0.7.0", sha256="0283391526a91c084249ab4d752e2de361a77677e1b435041fae479454e371c3")
    version("0.6.2", sha256="2bb75a65edae028879775afb435d397ebad0122bbf2a23a5138844998fe74fda")
    version("0.6.1", sha256="bc5e608ff33d59c9583964e453be83652b9ee9621ae3f69dbbd14798c1baac20")
    version("0.6.0", sha256="4a24e331f502a41b59751fe460a74e1dd4a8a7eb39ada3c00db94b96e2b841aa")
    version("0.5.1", sha256="55e52f31a518da5300af0555660b4566512630306d13a9e8430d9abde569c15e")
    version("0.5.0", sha256="b6afac6dccc2fcb3df52e42b25b881f0d3833b221c90d0258ed28851e0cf1d42")
    version("0.4.0", sha256="8d9e3befedead497dd77c198bbbf26baa8ae8bd1761c716f90e342c4a9a76add")
    version("0.3.4-1", sha256="3883dd81eb13290df6914cc25c98aced2f3bd44d6c6015d84864195c6628f8f8")
    version("0.3.4", sha256="d8d37af7c972b0c3a71b74fc5ffd4e14fe4939c166cd94074b2b3082aa7b2084")
    version("0.3.2-2", sha256="4c3584abacb5f0981b09253752d7882a581d73765962d9786e339cef5fd99a69")
    version("0.3.2-1", sha256="bacb278ded80e64aebd811f3c50eeca2d96a91cc88a5d534a74164ac08bf1ffc")
    version("0.3.2", sha256="196bd81c5639863d6dc37407dd777fc107bcf3ee7d954253a8f5ce6a3be7a771")
    version("0.3.1-1", sha256="0f23733e8d75cd103a39ec3ee9e88ed121c2f5c4f44e830f901e76f0e81634ed")
    version("0.3.1", sha256="87e710b606f625eb6d421f5be4e06aa414c0eef86ced44b03b61a381a1c1481b")
    version("0.3.0", sha256="9dbde43b4c190c1a4b42472eb1ea6b89eec9de64ae4e73f36facc267f1147b1d")
    version("0.2.9", sha256="569d459e030bc5e1220f9ab7c671cf814cfb5afe8e3876c9320e484c1a9dd650")
    version("0.2.8", sha256="25734c6c1f26176fe3cce96d93de1c8e401275b25c457b4cb38a849760ebe64a")
    version("0.2.7", sha256="96d01aaf492bd66d6f7cf31638451ba5536d989314789903cc480e80ad53bca3")
    version("0.2.6", sha256="5cf2af519f349b54f3e91f143214aece31febf8d96720d3b29cd2def49ae1584")
    version("0.2.5", sha256="13ba53b22dbcda041d57f3d15ec96eae5a98e8529a031e3b584629515dc51918")
    version("0.2.4", sha256="d67dcb09ff87a58364fa7e4d6d7393a6370e79551f0fe4e679a28c0703c7defe")
    version("0.2.3", sha256="4d905f97fe1a45228130032da72b0061d2f94f65ee1534e77dc1aa69420a7a5a")
    version("0.2.2-1", sha256="b1a0ad076e2dfca76d9916be399394563596a39cc44a8455ebb61988f64b94b3")
    version("0.2.2", sha256="7c16ba603d3d03c787440565df2f9a55d34035462021c4d8aa1a51b6e132c01c")
    version("0.2.1-2", sha256="92e7c15cfa3832f8ae3d84fa1f924be09cced508bee0cf6b4e6dc085ddf5323e")
    version("0.2.1", sha256="851832b999dd70945840ea9f4c1bf07ea12e411055d9883aa3d053877316b307")

    depends_on("r-arrow@13.0.0:", type=("build", "run"))
    depends_on("r-bit64", type=("build", "run"))
    depends_on("r-callr", type=("build", "run"))
    depends_on("r-dbitest", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-dbplyr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-vctrs", type=("build", "run"))
    depends_on("r-withr", type=("build", "run"))
