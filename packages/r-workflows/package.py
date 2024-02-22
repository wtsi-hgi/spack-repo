# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWorkflows(RPackage):
	"""Modeling Workflows

	Managing both a 'parsnip' model and a preprocessor, such as a
    model formula or recipe from 'recipes', can often be challenging. The
    goal of 'workflows' is to streamline this process by bundling the
    model alongside the preprocessor, all within the same object.
	"""
	
	homepage = "https://github.com/tidymodels/workflows"
	cran = "workflows" 

	version("1.1.4", md5="6e78b96d1969bfd9f87c841a8a36464d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli@3.3:", type=("build", "run"))
	depends_on("r-generics@0.1.2:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-hardhat@1.2:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-modelenv@0.1:", type=("build", "run"))
	depends_on("r-parsnip@1.2:", type=("build", "run"))
	depends_on("r-rlang@1.0.3:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-vctrs@0.4.1:", type=("build", "run"))
