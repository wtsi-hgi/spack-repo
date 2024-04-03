# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuickplot(RPackage):
	"""A System of Plotting Optimized for Speed and Modularity.

	A high-level plotting system, built using 'grid' graphics, that is
	optimized for speed and modularity. This has great utility for quick
	visualizations when testing code, with the key benefit that visualizations
	are updated independently of one another."""

	cran = "quickPlot"

	maintainers("dorton21")
	version("0.1.8", sha256="5927186ebbd86d2282c59dd28c4af6977ae5f9bc5766de8fce34b94bbfe33be7")
	version("0.1.6", sha256="48690a77ae961ed1032130621ef06b2eaf86ee592bf1057471a8c6d6a98ace55")
	version("1.0.2", md5="bd5e5d18c2548a28d6e519e646f740d2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-fpcompare", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
