# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRvcg(RPackage):
	"""Manipulations of Triangular Meshes Based on the 'VCGLIB' API

	Operations on triangular meshes based on 'VCGLIB'. This package
    integrates nicely with the R-package 'rgl' to render the meshes processed by
    'Rvcg'. The Visualization and Computer Graphics Library (VCG for short) is
    an open source portable C++ templated library for manipulation, processing
    and displaying with OpenGL of triangle and tetrahedral meshes. The library,
    composed by more than 100k lines of code, is released under the GPL license,
    and it is the base of most of the software tools of the Visual Computing Lab of
    the Italian National Research Council Institute ISTI <https://vcg.isti.cnr.it/>,
    like 'metro' and 'MeshLab'. The 'VCGLIB' source is pulled from trunk
    <https://github.com/cnr-isti-vclab/vcglib> and patched to work with options
    determined by the configure script as well as to work with the header files
    included by 'RcppEigen'.
	"""
	
	homepage = "https://github.com/zarquon42b/Rvcg"
	cran = "Rvcg" 

	version("0.22.2", md5="c4603f1e0cb42e47db8a9ed3e71b6f92")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
