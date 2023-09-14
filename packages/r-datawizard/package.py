# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatawizard(RPackage):
    """A lightweight package to assist in key steps involved in any data analysis workflow: (1) wrangling the raw data to get it in the needed form, (2) applying preprocessing steps and statistical transformations, and (3) compute statistical summaries of data properties and distributions. """

    homepage = "https://easystats.github.io/datawizard/"
    cran = "datawizard"

    version("0.8.0", sha256="13a3ed4f36157b18955dcbcb5a1f81a0d913349312cd44141f0afde16a3d22a2")
    version("0.7.1", sha256="779cbcd1f799cb5ea7cd817b2e40a8441f6a7dda89083b6074cb1a0d3616c2ca")
    version("0.7.0", sha256="c05f25908d5f9968381a8b887f4dba7cfaa1f36de1d4f1797f21b46e038571a5")
    version("0.6.5", sha256="eb5124e77f48b49c1f990442df356d528938e389b4a78f75cc9c50e4eb468946")
    version("0.6.4", sha256="37852d11f8455737924a78033849984bc4519c04e74bb17dcf32d6bf10806347")
    version("0.6.3", sha256="279afa654e7f661ee428412b909aa1f74fcc592eff0640da18831227698fc932")
    version("0.6.2", sha256="8d97fca35502dd94e2e47aaeb0cb9b0ed4450985b42d3f57a80a6602aba45e90")
    version("0.6.1", sha256="f30b42e0b35fc6669d5a8077679a560ba3453a62ab098ab4d4b4bc6642c51467")
    version("0.6.0", sha256="91deca5ae2e0fed52c443f9b31da2f05bea6d8755fdd49fdd63ca27d6d8109e5")
    version("0.5.1", sha256="7cf89fe21bf9f4f51607e2a82ca90399a17eebafd9dd00c2aadc878b095812ac")
    version("0.5.0", sha256="f8b1a477192517df6898d0ca1f224023060ffea18a0524e2a0f5aeaf955b4b08")
    version("0.4.1", sha256="9d112d6de337c9be9fce9443d224c76a55737c24bc2dfebea3378bca55809e26")
    version("0.4.0", sha256="4a3ec3f9c493016d5a58a4c41d514eb2f53fb0f6741bff00ba1c9ffac3ee46c8")
    version("0.3.0", sha256="7a4517fd12b852473e0a061740d7a0ee46bcf2ae0a9a228805cd1858bd9bb9ca")
    version("0.2.3", sha256="3d8b3d33d6a462dd1d1757625f87017f9131b90c43bdbcc4b830f92fc8e79641")
    version("0.2.2", sha256="436d73f973eedd1279ba2ff0356700848ba79c08e149d066f938b9cf325da069")
    version("0.2.1", sha256="89ca06cca1e71245bbb7987e8149dedebe586af80f154decb5e9d8cddc875718")
    version("0.2.0.1", sha256="854ed3f69b2186d216e1b961c265d5c2646b65aaabacc9415849911e71480497")
    version("0.2.0", sha256="e317ad23328126ba9e90700ff3cdb1d9d940ff7bdb50693a686fe806a89c2baf")
    version("0.1.0", sha256="8300b5c61d795bdb9fd6ca8b0c1a92e7df7ced1634db4467317a9abab33a82b9")

    depends_on("r-insight", type=("build", "run"))
