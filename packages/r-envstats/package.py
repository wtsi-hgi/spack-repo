# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnvstats(RPackage):
	"""Package for Environmental Statistics, Including US EPA Guidance.

	Graphical and statistical analyses of environmental data, with  focus on
	analyzing chemical concentrations and physical parameters, usually in  the
	context of mandated environmental monitoring.  Major environmental
	statistical methods found in the literature and regulatory guidance
	documents,  with extensive help that explains what these methods do, how to
	use them,  and where to find them in the literature.  Numerous built-in
	data sets from  regulatory guidance documents and environmental statistics
	literature.  Includes  scripts reproducing analyses presented in the book
	"EnvStats:  An R Package for  Environmental Statistics" (Millard, 2013,
	Springer, ISBN 978-1-4614-8455-4,
	<https://www.springer.com/book/9781461484554>)."""

	cran = "EnvStats"

	version("2.8.1", md5="e55d55f0e9a74b71fef89416f4e4bc6c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
