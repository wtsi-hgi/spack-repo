# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RRmarkdown(RPackage):
	"""Dynamic Documents for R.

	Convert R Markdown documents into a variety of formats."""

	cran = "rmarkdown"
	version("2.9", sha256="6ce5af8b9a7c282619f74d3999d27ec4de12d3f93cde8fd12cc4c19f02ea8668")
	version("2.6", sha256="e6e799c472de11e079bc752cca4b4dbd6803650649457bb6ae836cb1edcdf6b0")
	version("2.26", md5="d4f5e42ce1e7d2ab04fb1beff82c4ff5")
	version("2.25", md5="c30424fc39406007031cf4e62ea572a8")
	version("2.21", sha256="c25b20a422d11a115c93460f41c488874002154abb349b14e0d6518682fdac28")
	version("2.17", sha256="aa576c458ec4c2e8468aaa4e3f60202d8d9c7ef54fa01d6b2d243bffee08c4be")
	version("2.16", sha256="d3d34e0419c419d3ab20eb60952a0f0f4c391d202277af55dcd673d25561fa71")
	version("2.14", sha256="e9ec17afa4d9d6e8cf555b56e0c00acc189d8ec0b4406680b14d71d62f0c3220")
	version("2.11", sha256="9371255300e7ea4cd936978ad2ca3d205d8605e09f4913cb0d4725005a7a9775")
	version("1.7", sha256="c3191db65b9ad41b6dbb77aff53487701032d306e92b208ef7515b747931fe63")
	version("1.14", sha256="f636b1048c5be56e06aa0b2b4342ad5c8192734f1e9b27468fef62be672edc61")
	version("1.13", sha256="96fb6b08d27bbb8054145e0a55721f905341941d4f6691480a2a234e2d5a63ef")
	version("1.0", sha256="ff1ecb74ebc444b9b0b7b547adc512daefe1ee08d06bc0e3ee4eb68e58d2ef30")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-bslib@0.2.5.1:", type=("build", "run"))
	depends_on("r-evaluate@0.13:", type=("build", "run"))
	depends_on("r-fontawesome@0.5:", type=("build", "run"))
	depends_on("r-htmltools@0.5.1:", type=("build", "run"))
	depends_on("r-jquerylib", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-knitr@1.43:", type=("build", "run"))
	depends_on("r-tinytex@0.31:", type=("build", "run"))
	depends_on("r-xfun@0.36:", type=("build", "run"))
	depends_on("r-yaml@2.1.19:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"), when="@:2.26")
	depends_on("pandoc@1.14:", type=("build", "link", "run"))
