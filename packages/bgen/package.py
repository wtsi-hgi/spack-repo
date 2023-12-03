# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Bgen(Package):
    """The library can be used as the basis for BGEN support in other software, or as a reference for developers writing their own implementations of the BGEN format."""

    homepage = "https://enkre.net/cgi-bin/code/bgen"
    fossil = "https://code.enkre.net/bgen"

    version("2022-09-10", tag="703a453117")

    depends_on("fossil", type="build")
    depends_on("waf", type="build")
    depends_on("bzip2")
    depends_on("zlib")
    depends_on("boost+system+thread+filesystem+date_time+chrono+timer")
    depends_on("sqlite")
    depends_on("zstd@1.1.0:")
    depends_on("pkg-config")

    def patch(self):
        for i in [" '3rd_party',", '"3rd_party/boost_1_55_0/boost/",', '"3rd_party/zstd-1.1.0/",', '"3rd_party/sqlite3/",']:
            filter_file(i, "", "./wscript", string=True)

        for i in ["db/src/SQLite3Statement.cpp", "db/src/SQLStatement.cpp", "db/include/db/SQLite3Connection.hpp", "db/include/db/SQLStatement.hpp", "db/include/db/SQLite3Statement.hpp"]:
            filter_file('"sqlite3/sqlite3.h"', '<sqlite3.h>', i)

        filter_file("std::ios::streampos", "std::streampos", "src/View.cpp", string=True)
        filter_file("(total_count == 0)", "(*total_count == 0)", "appcontext/src/CmdLineUIContext.cpp", string=True)
        filter_file('"zstd.h"', "<zstd.h>", "genfile/include/genfile/zlib.hpp", string=True)

    def setup_build_environment(self, env):
    	env.set("USER", "user")
        env.set("LDFLAGS", "-lzstd -lsqlite3 -lboost_system -lboost_thread -lboost_filesystem -lboost_date_time -lboost_chrono -lboost_timer")

    def install(self, spec, prefix):
        waf = which("waf")

        waf("configure", "--prefix", prefix)
        waf()
        waf("install")
        install_tree(".", prefix)
