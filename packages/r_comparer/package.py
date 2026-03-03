# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComparer(RPackage):
	"""Compare Output and Run Time

	Quickly run experiments to compare the run time and output of
    code blocks. The function mbc() can make fast comparisons of code,
    and will calculate statistics comparing the resulting outputs.
    It can be used to compare model fits to the same data or
    see which function runs faster.
    The R6 class ffexp$new() runs a function using all possible combinations
    of selected inputs. This is useful for comparing the effect of
    different parameter values. It can also run in parallel and
    automatically save intermediate results, which is very useful
    for long computations.
	"""
	
	homepage = "https://github.com/CollinErickson/comparer"
	cran = "comparer" 

	version("0.2.3", md5="6a3f2b98f38db8f1efaf9f72dc4d1428")

	depends_on("r-r6", type=("build", "run"))
