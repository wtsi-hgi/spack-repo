# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArrow(RPackage):
    """Integration to 'Apache' 'Arrow'.

    'Apache' 'Arrow' <https://arrow.apache.org/> is a cross-language development
    platform for in-memory data. It specifies a standardized columnar memory
    format organized for efficient analytic operations on modern hardware. This
    package provides an interface to the 'Arrow C++' library.
    """

    homepage = "https://arrow.apache.org/docs/r/"
    cran = "arrow"

    version("22.0.0", sha256="6a864f5c8b2c77394de2ea8f9b8705b8163f0de00bcbfd1b4f393106fd8ea8ab")
    version("15.0.1", sha256="7f45843c820ff0418f9c64da6d9f82d1f14d7aceaf5032de3d3206582eb8171c")
    version("14.0.0.2", sha256="7138a52d66f1b94ec31c25e8929d6f92b1640df852a10817600a82ab68ba8ab7")

    depends_on("r@4.1:", type=("build", "run"))

    with default_args(type=("build", "run")):
        depends_on("r-assertthat")
        depends_on("r-bit64@0.9.7:")
        depends_on("r-cpp11@0.4.2:")
        depends_on("r-glue")
        depends_on("r-purrr")
        depends_on("r-r6")
        depends_on("r-rlang@1.0.0:")
        depends_on("r-tidyselect@1.0.0:")
        depends_on("r-vctrs")

    depends_on("curl", type=("build", "link", "run"))
    depends_on("openssl", type=("build", "link", "run"))
    depends_on("cmake@3.26:", type="build")
