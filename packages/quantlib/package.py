# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Quantlib(CMakePackage):
    """QuantLib: the free/open-source library for quantitative finance."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.quantlib.org"
    url = "https://github.com/lballabio/QuantLib/archive/refs/tags/v1.33.tar.gz"

    version("1.33", sha256="f973831d951b815a30392113c7cab7b66e6e2ea05dd12e3cb7c3b7ca3b20b081")
    version("1.32", sha256="987766b8303817284b93eb26027a488d01dd824d687d879dcf68ffde4b27fb9b")
    version("1.31.1", sha256="ed3813881ab42cc5a1639f95319a54dd337ab5e1c5cf0e5e673517bd1d880fc6")
    version("1.31", sha256="c148ded01cfe78e11c78dd2eeecd03e686a297be659e5ec4949a1db569cc680f")

    depends_on("boost")
