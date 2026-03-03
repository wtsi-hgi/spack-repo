# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGitlabr(RPackage):
	"""Access to the 'Gitlab' API

	Provides R functions to access the API of the project and
    repository management web application 'GitLab'. For many common tasks
    (repository file access, issue assignment and status, commenting)
    convenience wrappers are provided, and in addition the full API can be
    used by specifying request locations. 'GitLab' is open-source software
    and can be self-hosted or used on <https://about.gitlab.com>.
	"""
	
	homepage = "https://statnmap.github.io/gitlabr/"
	cran = "gitlabr" 

	version("2.0.1", md5="49ab31a1a2cd2939a57a96341d16c7d0")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-arpr", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-dplyr@0.4.3:", type=("build", "run"))
	depends_on("r-httr@1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr@0.2.2:", type=("build", "run"))
	depends_on("r-shiny@0.13:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble@1.1:", type=("build", "run"))
