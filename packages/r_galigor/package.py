# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaligor(RPackage):
	"""Collection of Packages for Internet Marketing

	Collection of packages for work with API 'Google Ads' <https://developers.google.com/google-ads/api/docs/start>, 
    'Yandex Direct' <https://yandex.ru/dev/direct/>, 'Yandex Metrica' <https://yandex.ru/dev/metrika/>, 
    'MyTarget' <https://target.my.com/help/advertisers/api_arrangement/ru>, 'Vkontakte' <https://vk.com/dev/methods>, 
    'Facebook' <https://developers.facebook.com/docs/marketing-apis/> and 'AppsFlyer' <https://support.appsflyer.com/hc/en-us/articles/207034346-Using-Pull-API-aggregate-data>. 
    This packages allows you loading data from ads account and manage your ads materials.
	"""
	
	homepage = "https://selesnow.github.io"
	cran = "galigor" 

	version("0.2.5", md5="7babca16f30fd10f8fb086a0ffc68f50")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
	depends_on("r-rstudioapi@0.7:", type=("build", "run"))
	depends_on("r-tibble@1.4.2:", type=("build", "run"))
	depends_on("r-gargle@1.2:", type=("build", "run"))
	depends_on("r-ryandexdirect", type=("build", "run"))
	depends_on("r-rfacebookstat", type=("build", "run"))
	depends_on("r-rvkstat", type=("build", "run"))
	depends_on("r-rmytarget", type=("build", "run"))
	depends_on("r-rym", type=("build", "run"))
	depends_on("r-getproxy", type=("build", "run"))
	depends_on("r-rgoogleads", type=("build", "run"))
	depends_on("r-rappsflyer", type=("build", "run"))
