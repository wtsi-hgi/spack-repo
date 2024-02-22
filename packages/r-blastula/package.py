# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlastula(RPackage):
	"""Easily Send HTML Email Messages

	Compose and send out responsive HTML email messages that render
    perfectly across a range of email clients and device sizes. Helper functions
    let the user insert embedded images, web link buttons, and 'ggplot2' plot
    objects into the message body. Messages can be sent through an 'SMTP'
    server, through the 'RStudio Connect' service, or through the 'Mailgun' API
    service <https://www.mailgun.com/>.
	"""
	
	homepage = "https://github.com/rstudio/blastula"
	cran = "blastula" 

	version("0.3.4", md5="daccccb2e48814c2c049391a9254b327")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-base64enc@0.1.3:", type=("build", "run"))
	depends_on("r-commonmark@1.7:", type=("build", "run"))
	depends_on("r-curl@4.3:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-fs@1.3.1:", type=("build", "run"))
	depends_on("r-getpass@0.2.2:", type=("build", "run"))
	depends_on("r-here@0.1:", type=("build", "run"))
	depends_on("r-htmltools@0.4:", type=("build", "run"))
	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-mime@0.6:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-uuid@0.1.2:", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
