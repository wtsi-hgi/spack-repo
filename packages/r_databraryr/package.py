# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatabraryr(RPackage):
    """Interact with the 'Databrary.org' API

          'Databrary.org' is a restricted access repository for research data, especially video and audio.
    This package provides commands to interact with the data stored on 'Databrary.org'.
    """

    homepage = "https://databrary.github.io/databraryr/"
    cran = "databraryr"

    version("0.6.3", md5="7b81de7b59f55f621ae4bb203cc91c83")
    version("0.6.1", md5="6f319aab4e5e18080d56a5f0e7d4e303")
    version("0.6.0", md5="6f012c806a50d58a03f9ce37b4f9f59f")

    depends_on("r@4.3.2:", type=("build", "run"))
    depends_on("r-dplyr@1.1.4:", type=("build", "run"))
    depends_on("r-httr@1.4.7:", type=("build", "run"))
    depends_on("r-httr2@1:", type=("build", "run"))
    depends_on("r-rvest@1.0.3:", type=("build", "run"))
    depends_on("r-jsonlite@1.8.8:", type=("build", "run"))
    depends_on("r-keyring@1.3.2:", type=("build", "run"))
    depends_on("r-stringr@1.5.1:", type=("build", "run"))
    depends_on("r-magick@2.8.2:", type=("build", "run"))
    depends_on("r-tibble@3.2.1:", type=("build", "run"))
    depends_on("r-plyr@1.8.9:", type=("build", "run"))
    depends_on("r-purrr@1.0.2:", type=("build", "run"))
    depends_on("r-lifecycle@1.0.4:", type=("build", "run"))
    depends_on("r-assertthat@0.2.1:", type=("build", "run"))
    depends_on("r-getpass@0.2.4:", type=("build", "run"))
    depends_on("r-xfun@0.41:", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
