# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinr(RPackage):
	"""Cut Numeric Values into Evenly Distributed Groups

	Implementation of algorithms for cutting numerical values
    exhibiting a potentially highly skewed distribution into evenly distributed
    groups (bins). This functionality can be applied for binning discrete
    values, such as counts, as well as for discretization of continuous values,
    for example, during generation of features used in machine learning
    algorithms.
	"""
	
	homepage = "https://github.com/jabiru/binr"
	cran = "binr" 

	version("1.1.1", md5="51b205731c7101342207cf31a01b3d57")

	depends_on("r@2.15:", type=("build", "run"))
