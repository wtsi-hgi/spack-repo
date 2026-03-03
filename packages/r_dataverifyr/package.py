# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataverifyr(RPackage):
	"""A Lightweight, Flexible, and Fast Data Validation Package that
Can Handle All Sizes of Data

	Allows you to define rules which can be used to verify a given
    dataset.
    The package acts as a thin wrapper around more powerful data packages such
    as 'dplyr', 'data.table', 'arrow', and 'DBI' ('SQL'), which do the heavy lifting.
	"""
	
	homepage = "https://github.com/DavZim/dataverifyr"
	cran = "dataverifyr" 

	version("0.1.8", md5="eac7cc140a9b91a513cc45f4c5cfadb4")

	depends_on("r-yaml", type=("build", "run"))
