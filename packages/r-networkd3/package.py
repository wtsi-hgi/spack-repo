# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install r-networkd3
#
# You can edit this file again by typing:
#
#     spack edit r-networkd3
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RNetworkd3(RPackage):
    """D3 JavaScript network graphs from R.

    Create D3 JavaScript network, sankey, dendrogram, and chord diagrams
    from R using the htmlwidgets framework."""

    homepage = "https://christophergandrud.github.io/networkD3/"
    cran = "networkD3"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    license("MIT")

    version("0.4.1", sha256="5be36aa5dd3722b1cd52a149c50af2dbef0714b2dab2b4dbf7552c628925f64e")
    version("0.4", sha256="33b82585f1eec6233303ec14033a703d0b17def441c7a0a67bf7e6764c9c9d0b")
    version("0.3", sha256="6f9d6b35bb1562883df734bef8fbec166dd365e34c6e656da7be5f8a8d42343c")
    version("0.2.13", sha256="e16543d47569ec680f0623df85110e72216c2c67fa9e1433bfa19cc3cc73642f")
    version("0.2.12", sha256="b81b59c3c992609e25e1621e51d1240e3d086c2b9c3e9da49a6cb0c9ef7f4ea5")
    version("0.2.11", sha256="e8abc48d2726f6534255e173e1ce695a78abcbe86029057035281188b30fc2aa")
    version("0.2.10", sha256="7b9e5c4b26b7c1464613d777327529c853f947ea8cd79a269e3a0c6c5f2e798a")
    version("0.2.8", sha256="32b7f52765d6fbbedcb65a845467d5fae48fa7ebe54f27719ac744a749577c70")
    version("0.2.6", sha256="0d78fd72a53c2608327a0dc7d253a139e0137893605a99713a699307de9f9b12")
    version("0.2.4", sha256="a56c6dd01379b088f7e0345c00d9516012177f422b3440a632eaac3b75ef3dd0")
    version("0.2.1", sha256="767bdf73cbd565a58ec1292f0f11d9a2bf11235f29bbf73e9bfa5efcb3bee43d")
    version("0.1.8", sha256="f0245cc7c1a35d5961010b80707fe90b45d54d8b64ca8efd8fd530de4817c5c2")
    version("0.1.7", sha256="295543d3fa235ed40fc76f293b744e4932d7c234595e9a7993040a57c9fe4a22")
    version("0.1.2.1", sha256="d5d54efe74ede8f468fa30733194fda38be3e2cfc8ac2dfa766d77b0d8c28375")
    version("0.1.1", sha256="d3a2c3d6594ee9fe5b7596299b4dedb743cfa9afc4f526414b14d5a3066654f7")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-htmlwidgets@0.3:", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-data-tree", type=("build", "run"))
