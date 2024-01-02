# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RVctrs(RPackage):
    """Defines new notions of prototype and size that are used to provide tools for consistent and well-founded type-coercion and size-recycling, and are in turn connected to ideas of type- and size-stability useful for analysing function interfaces."""

    homepage = "https://github.com/r-lib/vctrs/issues"
    cran = "vctrs"

    version("0.6.3", sha256="93dc220dcde8b440586b2260460ef354e827a17dfec1ea6a9815585a10cfa5c2")
    version("0.6.2", sha256="feecabe11f6c55e04377d36fa59842187f0a6fe52aaf867c08289a948781ee84")
    version("0.6.1", sha256="77552463bd7c40af2618d635de6bb9ad1614d161a5e34d90167601dc5e8e1283")
    version("0.6.0", sha256="be0b712c4e6aae353120a60ded6a4301eb9631c8d256927b79b9ad83b4299757")
    version("0.5.2", sha256="76bf10243b9b31e23f56ffdaa1677a01767699e2098487f86bd42cb801d8c047")
    version("0.5.1", sha256="497982f717f21e7612b84940e95c282e2a96b942e6d47108f92cd92b7341db07")
    version("0.5.0", sha256="7c372e13c39ddace9c9bb9f33238de6dd2cd0f37dcc7054ba6435d271e5df686")
    version("0.4.2", sha256="5414d1d6977163b4e85efa40d6facdd98089d6ffd460daaba729d4200942d815")
    version("0.4.1", sha256="9676881e009aa1217818f326338e8b35dd9a9438918f8b1ac249f4c8afe460dd")
    version("0.4.0", sha256="89dee789aad9b06b2f314ece8de2d6c261a5cd5729a8a00be99d5b2b85c8542f")
    version("0.3.8", sha256="7f4e8b75eda115e69dddf714f0643eb889ad61017cdc13af24389aab2a2d1bb1")
    version("0.3.7", sha256="5ad9b3bcc77ca5153f21d406ea1503b38bd59e7f079c2e6c73bd0cd3c7ec1e0e")
    version("0.3.6", sha256="df7d368c9f2d2ad14872ba2a09821ec4f5a8ad77c81a0b05e1f440e5ffebad25")
    version("0.3.5", sha256="11605d98106e294dae1a9b205462dd3906a6159a647150752b85dd290f6635cc")
    version("0.3.4", sha256="eb47411c9e980a555f5819a7bce46896775df2ca7c9eaa7bf0a9c16f067b7877")
    version("0.3.3", sha256="1b68a621a2bd47d53738934ceee58bb035844f528f65e3b1a4df1dc15e0dd904")
    version("0.3.2", sha256="624599bda2f44af65cf6ae31235692da57b46d039ed4c308a95149a2ebd84817")
    version("0.3.1", sha256="17e6358735504166ecb1aab581e5fa5e565ffb6f10e8a12c4d476a8e1f8aba08")
    version("0.3.0", sha256="f6ee13245e2507049706d3f45efa8d63cadae5359de3bfdcb5cccc5ac074c12b")
    version("0.2.4", sha256="dcc8b6bfd2d951d48d338a3d4deaaabfee356c0ee43169a6d6b06ea78cfe4f97")
    version("0.2.3", sha256="1c716d100a6c8e7f5aaa025ff4a5bd001b4da72ab71b85070259f31b6eb7d2de")
    version("0.2.2", sha256="0dab9120ba88ad98acd91248568f541c5715e93a4c753ec0a8bba82269951d01")
    version("0.2.1", sha256="e04f0b16c265fd0af8660b8768c8f53fded638a61c624a642d7a6cb8b7939c66")
    version("0.2.0", sha256="5bce8f228182ecaa51230d00ad8a018de9cf2579703e82244e0931fe31f20016")
    version("0.1.0", sha256="cc28febd74b4c7800076ac4d2c628755125981bdd3ebf295bb3952753fca818f")

    depends_on("r-cli@3.4.0:", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
    depends_on("r-rlang@1.1.0:", type=("build", "run"))
