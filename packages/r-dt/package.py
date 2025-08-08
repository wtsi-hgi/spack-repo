# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDt(RPackage):
    """A Wrapper of the JavaScript Library 'DataTables'.

    Data objects in R can be rendered as HTML tables using the JavaScript
    library 'DataTables' (typically via R Markdown or Shiny). The 'DataTables'
    library has been included in this R package. The package name 'DT' is an
    abbreviation of 'DataTables'."""

    cran = "DT"
    version("0.33", sha256="e145dadb1ce3db7c837f4313a8b5615b5b8ae63063ec2df93e528529717b27b8")
    version("0.32", sha256="41d0b9575db7bd4e4ca6a88149faa306b980043eca15044680690542d812725b")
    version("0.31", sha256="956f42a784d1c426ddc75ebfb22a854886e2d6ae8b7014b95669aed0cd699c87")
    version("0.30", sha256="2f1a53e32a9b493efc9041758810c6a744ebb17ad7a942b376389b7e95ff698e")
    version("0.29", sha256="a8d26de14be182c7dcb447122d5364fe92a9e62ee6ed2cd254aaa72d33d438ad")
    version("0.28", sha256="d975d57dd8523c021dbd815c8369f174aef47b9850bb4bdb9929be3d83a00d4e")
    version("0.27", sha256="e32fdccd2be430933cff88a9ce79045bfdbe3e08e0cd8d15037445808613289a")
    version("0.26", sha256="c412932be126d44f415559258e1d65adc0e84c3dfb9a70ce3196a2f877f7030c")
    version("0.25", sha256="0dfc8713062e1fe4e0428936367f35a0a41616c27b6d9b002bdfda58091c442b")
    version("0.24", sha256="0cd74c94849f577489cd2b5fbe44ca8946d29ecafe7e7a0b437e4c984dea6763")
    version("0.23", sha256="360ae2fcb1141125a1b16448570fc37d14c4dd3f78a872c26df4fda1787cdc70")
    version("0.22", sha256="3f181c4ef8dd225864c8859751cd369a21d37b83bd33a35922723f0f0c045099")
    version("0.21", sha256="f65748b85570949acc729d81d30a30f7e2dc0545a9ecd624e6e87c0413bc14fa")
    version("0.20", sha256="c66d7f49ec101fdbb91c6d26c06fb1373f9ebdefe29fe99f2ae1a641220aba9f")
    version("0.19", sha256="baa6bdae215ab84a5dee9c0a6c55dd92135c795d13dfce3c3485519c6f0e3b13")
    version("0.18", sha256="219039f7bc4e1c854b7f394152641b9f3a4c747891899a864993801280acb8ef")
    version("0.17", sha256="e3430292421dcc2b6ad5f2deda729f0603da4eb31f86d071833e6e11abf3fb56")
    version("0.16", sha256="734df36b9de54ebb90d932930a1ba960028759100ac8e7a59897ac6ec968c446")
    version("0.15", sha256="f3e0060bcac0dee7c9ed8a1037171166ed83953f042501c32931003b715482f1")
    version("0.14", sha256="4bad6d17b06d989b85bf87c9d45cbbf76c8711c9e372ed78892a6bc50fb71176")
    version("0.13", sha256="79a073fe96980ce150d790ab76133c9e80bd463270c34d149c03934a622d63b5")
    version("0.12", sha256="239906a884a485fd09e50bf10a52268f62ffd4ba9569499c4d92055511120901")
    version("0.11", sha256="6fee5a23b1a574413b3532d13b9df1b31e91f752416a0406bb2a40a50ed06926")
    version("0.10", sha256="3cc6dfc9697b52aef21d30dcfd355831c6216edcc6dd6bfb9a106cce6ab0906f")
    version("0.9", sha256="47a16655f13392bdcfd6a0712c7e77457400796e0a39625dad684b600ab10a9e")
    version("0.8", sha256="90195054148806cf31c7db5c41f72d5389c75adc0b1183606a9babd2c6ae8e21")
    version("0.7", sha256="1de3f170deccd9e3aaefc057dd87c498e3b3f7f88eff645cf165ac34ffe3de2c")
    version("0.6", sha256="2ed68e9d161559171fa74b6105eee87b98acf755eae072b38ada60a83d427916")
    version("0.5", sha256="0e5bbb91b88a769e52ba079ebac266a25ea0f0a23bdf3deff31f51d2a81eade8")
    version("0.4", sha256="3daa96b819ca54e5fbc2c7d78cb3637982a2d44be58cea0683663b71cfc7fa19")
    version("0.3", sha256="ef42b24c9ea6cfa1ce089687bf858d773ac495dc80756d4475234e979bd437eb")
    version("0.2", sha256="a1b7f9e5c31a241fdf78ac582499f346e915ff948554980bbc2262c924b806bd")
    version("0.1", sha256="129bdafededbdcc3279d63b16f00c885b215f23cab2edfe33c9cbe177c8c4756")

    depends_on("r-htmltools@0.3.6:", type=("build", "run"))
    depends_on("r-htmlwidgets@1.3:", type=("build", "run"))
    depends_on("r-httpuv", type=("build", "run"))
    depends_on("r-jsonlite@0.9.16:", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-crosstalk", type=("build", "run"))
    depends_on("r-jquerylib", type=("build", "run"))
    depends_on("r-promises", type=("build", "run"))
