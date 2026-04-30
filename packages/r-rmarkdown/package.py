# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RRmarkdown(RPackage):
	"""Dynamic Documents for R.

	Convert R Markdown documents into a variety of formats."""

	cran = "rmarkdown"
    version("2.31", sha256="0c5baed4a447292f15507794d2dde6b18bae1fa6c45ea6ada8bcd99ca211fcbc")
    version("2.30", sha256="4d2ad3d230c1a9ded394dff76cbaf83a66bb8d96493b8d11cd56be78afa5a338")
    version("2.29", sha256="6662ac85316c869caad6e3b95468cad97f6eef106d47b066db8d40c05a490928")
    version("2.28", sha256="a102a503a92d4203038c5a0675451daf9460df18efcabd5c23283ecefe75a085")
    version("2.27", sha256="61e9cb3eab4f8587fea98d3358652695b7e77eda858caa4c8985241ba6502b9f")
    version("2.24", sha256="3873efa46df4b1d2613b49d345d6442cd1a332e08594c204c8fa177edcd53d86")
    version("2.23", sha256="668d086f0ca597ef6f665b471f19b176be45971828b74ec8c25c3a46947bc825")
    version("2.22", sha256="c6635519503e0fcdd518696d3ac96d8d28d9d4ecd9db0532c53426002f6387b8")
    version("2.20", sha256="d7f7059bfcb43e4b92432d69ba0e0c74ad10a20f153689262a3e848adb60159d")
    version("2.19", sha256="39c2a4c51de8c65886a7a3d7e44c3d21167069a89ee26c0f5db8243b70db9b92")
    version("2.18", sha256="4faa7ae626defb5b066002a1782d30d2a9f42d8d9e51779c0b94d263cffa8f22")
    version("2.15", sha256="6af64f5865f691ccfb864c0255a9fa9193234fb6a44f4955d664930ca92cf598")
    version("2.13", sha256="7217bea1d202b34a9994b2e068a7da063d5e3b1e0cfada89125aecdedbb80744")
    version("2.12", sha256="c3aba9eda862483c7631485002b6b94e0076e4fdd2384a095ee30243b958e690")
    version("2.10", sha256="53a65942faaeca21e5232b86cea6b8624069913e4c1946e87c0624a97d624cdc")
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
	depends_on("r-stringr", type=("build", "run"), when="@:2.25")
	depends_on("pandoc@1.14:", type=("build", "link", "run"))
