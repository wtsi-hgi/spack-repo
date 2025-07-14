# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandrotation(RPackage):
	"""Random Rotation Methods for High Dimensional Data with Batch Structure

	A collection of methods for performing random rotations on high-dimensional, normally distributed data (e.g. microarray or RNA-seq data) with batch structure. The random rotation approach allows exact testing of dependent test statistics with linear models following arbitrary batch effect correction methods.
	"""
	
	homepage = "https://github.com/phettegger/randRotation"
	bioc = "randRotation"

	version("1.20.0", commit="f882e56088aad962c16770ea4f2545f8206dee4e")
	version("1.14.0", commit="d16400288cfcb82a759af9102cea1c74146a100f")

	depends_on("r-rdpack@0.7:", type=("build", "run"))
