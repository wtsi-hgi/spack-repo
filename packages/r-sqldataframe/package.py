# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqldataframe(RPackage):
    """Representation of SQL database in DataFrame metaphor

    SQLDataFrame is developed to lazily represent and efficiently analyze SQL-based tables in _R_. SQLDataFrame supports common and familiar 'DataFrame' operations such as '[' subsetting, rbind, cbind, etc.. The internal implementation is based on the widely adopted dplyr grammar and SQL commands. In-memory datasets or plain text files (.txt, .csv, etc.) could also be easily converted into SQLDataFrames objects (which generates a new database on-disk).
    """

    homepage = "https://github.com/Bioconductor/SQLDataFrame"
    bioc = "SQLDataFrame"

    version("1.22.0", commit="f4c9c9fc2e95911af1a355c94128881038986bf0")
    version("1.16.1", commit="4a69da1296144a392fb95411ce40cb7cef28bda8")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
    depends_on("r-dbplyr@1.4:", type=("build", "run"))
    depends_on("r-s4vectors@0.33.3:", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-lazyeval", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    # Missing runtime deps discovered during install
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-duckdb", type=("build", "run"))
