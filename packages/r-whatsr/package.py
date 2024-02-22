# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWhatsr(RPackage):
	"""Parsing, Anonymizing and Visualizing Exported 'WhatsApp' Chat
Logs

	Imports 'WhatsApp' chat logs and parses them into
    a usable dataframe object. The parser works on chats exported 
    from Android or iOS phones and on Linux, macOS and Windows. The parser has  multiple options for extracting smileys and emojis
    from the messages, extracting URLs and domains from the messages, extracting names and types of sent 
    media files from the messages, extracting timestamps from messages, extracting and anonymizing author 
    names from messages. Can be used to create anonymized versions of data.
	"""
	
	cran = "WhatsR" 

	version("1.0.4", md5="85892ce8e564027e51145e92533b62c8")

	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-qdapregex", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tokenizers", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-anytime", type=("build", "run"))
	depends_on("r-mgsub", type=("build", "run"))
	depends_on("r-qdap", type=("build", "run"))
	depends_on("r-ggwordcloud", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ragg", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-ggmap", type=("build", "run"))
