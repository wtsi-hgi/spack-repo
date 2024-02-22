# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlackr(RPackage):
	"""Send Messages, Images, R Objects and Files to 'Slack'
Channels/Users

	'Slack' <https://slack.com/> provides a service for teams to
    collaborate by sharing messages, images, links, files and more.
    Functions are provided that make it possible to interact with the
    'Slack' platform 'API'. When you need to share information or data
    from R, rather than resort to copy/ paste in e-mails or other services
    like 'Skype' <https://www.skype.com/en/>, you can use this package to
    send well-formatted output from multiple R objects and expressions to
    all teammates at the same time with little effort. You can also send
    images from the current graphics device, R objects, and upload files.
	"""
	
	homepage = "https://github.com/mrkaye97/slackr"
	cran = "slackr" 

	version("3.3.1", md5="e9a9428011e8b3143a38df36a0e1d6aa")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-cachem@1.0.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr@1.4.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-memoise@2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
