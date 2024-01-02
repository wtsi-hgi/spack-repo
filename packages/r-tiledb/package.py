# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RTiledb(RPackage):
    """The TileDB R package offers an R interface to the storage engine of TileDB."""

    homepage = "https://tiledb-inc.github.io/TileDB-R/"
    url = "https://github.com/TileDB-Inc/TileDB-R/archive/refs/tags/0.21.1.tar.gz"

    version("0.21.1", sha256="3ede0a27b525df73aa22f352a22bfc0f0e862d0b604d7b7885188f9f201fd0e9")
    version("0.21.0", sha256="1bb67587a1529b429624f4ec63f020ea1f3cf4936e1af0b1d1262d9cdc002cc9")
    version("0.20.3", sha256="e79cb622860fe7fe2c283e111c68c7f8ccf217c0965b381720dede805c15cdf2")
    version("0.20.2", sha256="4242004cbd5b6018d67f3b08145015266ad8d79cb16e381b5627e70570a80913")
    version("0.20.1", sha256="bfa736ca408d5b11ad7a1634656c9f22e6acc9fb3f8903cf6980577d064b7d6c")
    version("0.20.0", sha256="d4aad6bfe38d6a9037d073c887c2f109dc4e89b9cff9924bbe47e5c934529eba")
    version("0.19.1", sha256="af40ff630c8f544f9f3b803b0a9bd0a6d1c45666fdf96fbc4d7c891cea509d84")
    version("0.19.0", sha256="e848dc052ff6978079c36a3f580be3ce2b7d9e9e7bf9050fd8c513c48d007a62")
    version("0.18.0", sha256="1310459f518d521a2488f93f328cbe7de02dd5e211a356548bb7216a6e52c597")
    version("0.17.1", sha256="db5417d35ec76dfd2497eef29d599b0a37173679e70408c0917de3e3a5caa589")

    depends_on("r-rcpp@1.0.8:", type=("build", "run"))
    depends_on("r-rcppint64", type=("build", "run"))
    depends_on("r-nanotime", type=("build", "run"))
    depends_on("r-spdl", type=("build", "run"))
    depends_on("r-tinytest", type=("build", "run"))
    depends_on("r-simplermarkdown", type=("build", "run"))
    depends_on("r-curl", type=("build", "run"))
    depends_on("r-bit64", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-palmerpenguins", type=("build", "run"))
    depends_on("r-nycflights13", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-arrow", type=("build", "run"))
