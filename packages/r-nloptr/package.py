# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNloptr(RPackage):
	"""R Interface to NLopt.

	Solve optimization problems using an R interface to NLopt. NLopt is a
	free/open-source library for nonlinear optimization, providing a common
	interface for a number of different free optimization routines available
	online as well as original implementations of various other algorithms. See
	<https://nlopt.readthedocs.io/en/latest/NLopt_Algorithms/> for more
	information on the available algorithms. Building from included sources
	requires 'CMake'. On Linux and 'macOS', if a suitable system build of
	NLopt (2.7.0 or later) is found, it is used; otherwise, it is built  from
	included sources via 'CMake'. On Windows, NLopt is obtained through
	'rwinlib' for 'R <= 4.1.x' or grabbed from the 'Rtools42 toolchain' for  'R
	>= 4.2.0'."""

	cran = "nloptr"

	version("2.0.3", md5="2c18f48b3c02c62126bd678134f8e501")

	depends_on("r-testthat", type=("build", "run"))
	depends_on("cmake@3.2.0:", type=("build", "link", "run"))
	depends_on("nlopt", type=("build", "link", "run"))

	def configure_args(self):
		include_flags = self.spec["nlopt"].headers.include_flags
		libs = self.spec["nlopt"].libs.libraries[0]
		args = [
			"--with-nlopt-cflags={0}".format(include_flags),
			"--with-nlopt-libs={0}".format(libs),
		]
		return args
