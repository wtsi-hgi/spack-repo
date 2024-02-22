# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFoundry(RPackage):
	"""'Palantir Foundry' Software Development Kit

	Interface to 'Palantir Foundry', including
    reading and writing structured or unstructured datasets, and more
    <https://www.palantir.com/platforms/foundry/>.
	"""
	
	homepage = "https://github.com/palantir/palantir-r-sdk"
	cran = "foundry" 

	version("0.13.0", md5="bdeefe00d4581bfdd0f07fab22bd44d3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-arrow@0.14:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
