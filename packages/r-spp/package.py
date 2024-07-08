# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.boost import Boost


class RSpp(RPackage):
    """Computes informative enrichment and quality measures for
    ChIP-seq/DNase-seq/FAIRE-seq/MNase-seq data. This is a modified version
    of r-spp to be used in conjunction with the phantompeakqualtools
    package."""

    homepage = "https://github.com/hms-dbmi/spp"
    url = "https://github.com/hms-dbmi/spp/archive/refs/tags/1.15.2.tar.gz"

    version("1.15.2", sha256="bf0d6f42d9461aeb7a20b1ddb12b57bc42d11732ca6f69ec3eb2157364cefd5b")

    depends_on("boost@1.41.0:")
    depends_on("r-catools", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("zlib-api", type=("build", "run", "link"))
    depends_on("r-rsamtools", type=("build", "run"))
