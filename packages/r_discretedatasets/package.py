# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscretedatasets(RPackage):
	"""Example Data Sets for Use with Discrete Statistical Tests

	Provides several data sets for use with discrete statistical tests
  and discrete multiple testing procedures. Some of them are also available as a
  four-column version, so that each row represents a 2x2 table.
	"""
	
	homepage = "https://github.com/DISOhda/DiscreteDatasets"
	cran = "DiscreteDatasets" 

	version("0.1.0", md5="c07ad9f48b0125349278ae19bc8c434e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
