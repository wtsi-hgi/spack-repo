# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffval(RPackage):
	"""Vegetation Patterns

	Find, visualize and explore patterns of differential taxa in
    vegetation data (namely in a phytosociological table), using the
    Differential Value (DiffVal). Patterns are searched through
    mathematical optimization algorithms. Ultimately, Total Differential
    Value (TDV) optimization aims at obtaining classifications of
    vegetation data based on differential taxa, as in the traditional
    geobotanical approach.  The Gurobi optimizer, as well as the R package
    'gurobi', can be installed from
    <https://www.gurobi.com/products/gurobi-optimizer/>.  The useful
    vignette Gurobi Installation Guide, from package 'prioritizr', can be
    found here:
    <https://prioritizr.net/articles/gurobi_installation_guide.html>.
	"""
	
	homepage = "https://gitlab.com/point-veg/diffval"
	cran = "diffval" 

	version("1.1.0", md5="320c3f68041b53f34fe147700c515d4c")

	depends_on("r@2.10:", type=("build", "run"))
