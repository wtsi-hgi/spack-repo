# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfigr(RPackage):
	"""An Implementation of Parsing and Writing Configuration File
(JSON/INI/YAML/TOML)

	
    Implements the JSON, INI, YAML and TOML parser for R setting and writing of configuration file. The functionality of this package is similar to that of package 'config'. 
	"""
	
	homepage = "https://github.com/Miachol/configr"
	cran = "configr" 

	version("0.3.5", md5="2f77cf4e70bf934f7fa4b4f35a51eebe")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-jsonlite@1.2:", type=("build", "run"))
	depends_on("r-ini@0.2:", type=("build", "run"))
	depends_on("r-yaml@2.1.3:", type=("build", "run"))
	depends_on("r-rcpptoml@0.1.3:", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
