# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerformance(RPackage):
    """Utilities for computing measures to assess model quality, which are not directly provided by R's 'base' or 'stats' packages."""

    homepage = "https://easystats.github.io/performance/"
    cran = "performance"

    version("0.10.5", sha256="d91c0dc1ab7e32868c750357b3af4e98f2bf972f724d9f6e50de4015c56f8caf")
    version("0.10.4", sha256="cabaea67c417b31361606ae4e98d1270160d4358f9bbb8a75f412efef374bc35")
    version("0.10.3", sha256="d8a8a0ee9d1a8af0adce0f981b88788b86958e3543a1c48b7e33a3f798c99ad0")
    version("0.10.2", sha256="4200c7f59d9eb2466ba2b95ca74beb244e461ad8b21401bc064eabe0f02d3d65")
    version("0.10.1", sha256="ff9ee7ddf034bc090501e03412eff3778641ee2e72f5096ac348d1e5ecff5fd4")
    version("0.10.0", sha256="0b66d18829a6f09ff9692ffba2db3c9f12e39f5f1fdd2bcf0e74c0137c39dd97")
    version("0.9.2", sha256="86eb0e04bc076b2e9f1f658d469e5514bc27ff6ccefa73195f143fdb82fbba39")
    version("0.9.1", sha256="de3e45fe2016017abcc3a697289f9f70291669009de028dcef6583037ef23876")
    version("0.9.0", sha256="9c67168e06900def7acf55249ec40f3f93444714aa666c241ddf6c794324d9fe")
    version("0.8.0", sha256="c2962bd51a6700ebe2bd62ceadb755154807ac641ecae77ca9d4395e31b452f6")
    version("0.7.3", sha256="5787348a701337cf3ef02914f9cb1da15ddfc75998c2a317c51c8e4e68d30d0f")
    version("0.7.2", sha256="24f9f360ba7471ba6f409812e9c72ef9aa36f8460054cb6a811c5b72d971cbf9")
    version("0.7.1", sha256="152b2f3213851126417e077f25401baf8b198a21589f852b7a2b6c99e9f9c8cd")
    version("0.7.0", sha256="d2affdb434c77ff3e081002fce0161267eab4872985fcd6a14ec9cf790df85fc")
    version("0.6.1", sha256="f61788da44a60440bc82959b56c3e59dbbb07fef38014ab27937a58c12fbe273")
    version("0.6.0", sha256="ec01166bfef3e4d4ecd814592a69250c1501811e85c123ef93b55e30cdbd212a")
    version("0.5.1", sha256="1d33b0b7b334815187e78b8eb3239045e96bb7caf1da768d30f470b8f6416cee")
    version("0.5.0", sha256="483865757f710498c4a1a9df6cabbf48996dd86426be2359a5309b268aad9a05")
    version("0.4.8", sha256="94c457593b3e2d7a23bd0f10a5c893dc719de4fa1bb4c7524d3273c06fa883be")
    version("0.4.7", sha256="b32c5b491f66177272f0315fe2e4f8a68486cd4c1f51eab7961b28517931813f")
    version("0.4.6", sha256="b2a3b61b4fc0eb1525d690d53ad73999501e0d9cfb8132855eca00f5f6b32922")
    version("0.4.5", sha256="1dbda59704b98fe949f695e92fed4ca780824322afe21354d8a33507b9addc48")
    version("0.4.4", sha256="8a1e1908845d173baa274cff451c64438b7ded3e487965bb9963e9cb8cf109a2")
    version("0.4.3", sha256="bf8d184af38e35cc7d39bcdff4117866b527a08bf314ab8e67d92eee0b2ac484")
    version("0.4.2", sha256="37159546817d622b96a4f61f6fd9bd9abe2335b965cf7f59db0d9d5031ae92dd")
    version("0.4.0", sha256="409365e17172fbc9b4d800ca1a7bad9771044cb666cce8761fb9d8aad3adb753")
    version("0.3.0", sha256="3c25dce5d550f05f27b4129efc39c509c76d09ea3d1aa4999aa0a40e9d23478e")
    version("0.2.0", sha256="3f34fb4fd95e1bed9d958fd73b0f95f52eda1768e3411d6217b9cb10cf37eddf")
    version("0.1.0", sha256="dcb2f3d2caaf5309a39706fb0c8c26bf0145c426181a98995f7fab098be88ea6")

    depends_on("r-bayestestr", type=("build", "run"))
    depends_on("r-insight", type=("build", "run"))
    depends_on("r-datawizard", type=("build", "run"))
