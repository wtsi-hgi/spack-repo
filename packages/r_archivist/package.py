# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArchivist(RPackage):
	"""Tools for Storing, Restoring and Searching for R Objects

	Data exploration and modelling is a process in which a lot of data
    artifacts are produced. Artifacts like: subsets, data aggregates, plots,
    statistical models, different versions of data sets and different versions
    of results. The more projects we work with the more artifacts are produced
    and the harder it is to manage these artifacts. Archivist helps to store
    and manage artifacts created in R. Archivist allows you to store selected
    artifacts as a binary files together with their metadata and relations.
    Archivist allows to share artifacts with others, either through shared
    folder or github. Archivist allows to look for already created artifacts by
    using it's class, name, date of the creation or other properties. Makes it
    easy to restore such artifacts. Archivist allows to check if new artifact
    is the exact copy that was produced some time ago. That might be useful
    either for testing or caching.
	"""
	
	homepage = "https://pbiecek.github.io/archivist/"
	cran = "archivist" 

	version("2.3.6", md5="45484525462d831083ba73f38e966574")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-flock", type=("build", "run"))
