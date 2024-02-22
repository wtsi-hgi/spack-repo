# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepo(RPackage):
	"""A Data-Centered Data Flow Manager

	A data manager meant to avoid manual storage/retrieval of
    data to/from the file system. It builds one (or more) centralized
    repository where R objects are stored with rich annotations,
    including corresponding code chunks, and easily searched and
    retrieved. See Napolitano (2017) <doi:10.1037/a0028240> for further
    information.
	"""
	
	cran = "repo" 

	version("2.1.5", md5="f118e72ced1a191e608a63c583a60b14")

	depends_on("r-digest", type=("build", "run"))
