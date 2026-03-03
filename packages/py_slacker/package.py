# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySlacker(PythonPackage):
    """Slack API client"""

    homepage = "http://github.com/os/slacker/"
    pypi = "slacker/slacker-0.9.9.tar.gz"

    version("0.1", sha256="1e401c612d90aeea70504b6eac649a904188907ea5f39a772e7dafc923dbd090")
    version("0.1.1", sha256="67b4bbb53b6f34ac8e2bc67261210f6c255ad4cf8ccffa4f6ccae1a63f1b772a")
    version("0.1.2", sha256="4bff8baae088aaa8762bc5acee3d15d8850124ad75e4c81846655cdd50c377ec")
    version("0.1.3", sha256="88d4048ef650a823bda5f83be3ab33cbd50da26c084751b4ca95d28cef6bb20a")
    version("0.1.4", sha256="ef3c75284ef9b2d5e26e6052d16d24635244149605dc68488f00c2abc7317602")
    version("0.1.6", sha256="069707a944c82261eed1c44bf289dcc6fcadab3507f14c17fd4bb9800f88e68d")
    version("0.1.7", sha256="c0edc12a2659d9d4e2b08df4d35f5370b994da815291defde9c32e77035aaf0c")
    version(
        "0.10.0",
        sha256="299e00c6da73e9c637674c4213ec71da9bbc75287bfcdaa37c4b6b255aa13abb",
        expand=False,
        url="https://files.pythonhosted.org/packages/f8/19/b2c2e71f6bb7972bdf96ab7d7c490f8c2c9de1db81d3c0eff60de6943d18/slacker-0.10.0-py3-none-any.whl",
    )
    version(
        "0.11.0",
        sha256="00a42970a0e75eb469f75265deb21a0df753916b1a2beff3983ab1993d4eaa3a",
        expand=False,
        url="https://files.pythonhosted.org/packages/b8/db/a4c59b69a1dde2abd1224636a24472b15e0a3a2af9727e9ea1ee71f402be/slacker-0.11.0-py3-none-any.whl",
    )
    version(
        "0.12.0",
        sha256="41ee24d0f28612542f9239b08d9936d0dee661d2a14e83d741037cb15fdf4ff4",
        expand=False,
        url="https://files.pythonhosted.org/packages/41/c5/006794554034d01c7821171a5f2fe3b233f3261d7af76abbfdb0d69f1ce8/slacker-0.12.0-py3-none-any.whl",
    )
    version("0.13.0", sha256="f4c55415096229c1cc616c1504d93672b05521e5499a9be26475e0a9a623c4dc")
    version("0.14.0", sha256="1ae7c597025c114e202b5c880345f150f795665bfc638010cac614ede4ed5108")
    version("0.2.0", sha256="640715133483e8a8be08484d1e6fb333f5eb04dc1d02e7df607fe47fff8a4a10")
    version("0.3.0", sha256="a7f0d2a528b4aad1ccbe2347cac30db0c2269703012fa3c0ce15c94249326bcf")
    version("0.3.1", sha256="62b9273ff83f37da0a2aeb588585279ae15af2219925a51d5e87db64abdd6557")
    version("0.3.3", sha256="03ae5ab9aed2e610866d36a4cb4e3ae0d7fa7637413a839aee3bcba98de2a871")
    version("0.3.7", sha256="339384762bb3b01c4950fc175eafd1613c87095062a92b9a10c4e9f3e5a6167e")
    version("0.3.9", sha256="4da3a9d07d46eabe3ce6b3ae459f2091e055c7b0ca1b76ade118898ab2701f82")
    version("0.4.0", sha256="88bebe5c12e9c2ba3a7e3043cd7163d7efa0a8b4de59e6af545d19476baafcb6")
    version("0.4.2", sha256="43c1fd89caaf016b279144af51e31ab7aa77339a62be8711b877bd30955a565a")
    version("0.5.0", sha256="74bb6d4cd9accef8007527becadd3a3f116bd00b5058e0d89d19f4e56ac5b884")
    version("0.5.1", sha256="d189f313671d945a5674976f0f268d64bde08bb982f83ef169d0473ec5fafcc6")
    version("0.5.4", sha256="276a9dc5e2dba7f5e1b021f4a1125bdc750ab39007317214b22e846ccd98be18")
    version("0.5.5", sha256="73271c32b98b81c4ca9cb5a56b7bbe33198583d97e01416d3c589a61c0c45c9a")
    version("0.5.6", sha256="963d647f8dad6e9d354967dec16a5c06ed67c27bf8e9814bf2369a2aa646773b")
    version("0.5.7", sha256="d7f77e5c60f85e739647d6bc181004bf663870c45919ff17580749c2cb84b95b")
    version("0.6.0", sha256="034df4fc2f04b8a9f6982f11bf064d1b344d6fa86e059b5b96291f5a5cd32bba")
    version("0.6.1", sha256="49239d51f0cdc57a9f8558714b66a285f9c9292f503fd8c8ae83bb053c7834e8")
    version("0.6.2", sha256="b9f3a7d45fb5f2ddb21d687c22c3ed1ab3127c2314009259d32bab721e746b5a")
    version("0.6.3", sha256="da7d242b64d1497cadc38c32cc51a1441d0a6b512c0b63dc3a596eec4a36a09a")
    version("0.6.8", sha256="e0192ece08968bcb5bff8fe51a4e1c1da95cd85c43bcfa41ec51e2940698743b")
    version("0.7.0", sha256="09fa26ba0025a5e710c13a4a2e50ccc4532d871ece033b755e572b96da87e244")
    version("0.7.3", sha256="806bc70355e0fb39a091a6e45bb86f280586bf5b01fd902e452779f09fbe66bc")
    version("0.7.4", sha256="f53136227b9cf32ab15329c0e7d7699d28883cbd541d0a1a893a4c305c63a972")
    version("0.7.9", sha256="a1c6d9eaf1fb8be76c7df78a3ee28dad6a809649a86193a8a325a7e97b376b88")
    version("0.8.6", sha256="3da946656c5925767b8e4b8c8a013594db407d1e32f6634b8a73ce4d88973e45")
    version("0.8.6.2", sha256="8f008d108fa4e45658689f91760527823211ce7fdfd18d1b5d2ced3edb953502")
    version("0.9.0", sha256="dd4cc667366ed66d24930c2f38f83c84336208e68059a245912df965a1b843db")
    version("0.9.10", sha256="d86119d35f0481e1e128087d65869a825ef984603c40fe94359d202fb99965e1")
    version("0.9.15", sha256="9c0985ce401424897f7e7205d07c685e8baf031b0185499e4e8f3c425a68b931")
    version("0.9.16", sha256="d745ae3ba3ecfad98f44687a82776bbea0ed6cc78e93a583cd39d3c64f586441")
    version("0.9.17", sha256="55e277b6911d34a81e0ef2badadf5909991a5050690146a4fdf55216d81205ab")
    version("0.9.18", sha256="372ebcef323eb8786240591d30da68cb890654ab38524078f5968e3b21f58a52")
    version("0.9.2", sha256="6181b458dcd6df103e546d1897e3af7786609dd2b8ca5e275071aea6fdc34b3b")
    version("0.9.21", sha256="b5389681f7cc62cd3cf9e6cff1c02a2eb6066c75ddc4bf871a14d76952b6bdbe")
    version("0.9.24", sha256="1cb679e8e401acd6d54571d1bbc9069eb762ef0d185c04969f91011caeb5667a")
    version("0.9.25", sha256="8b684ec943a2d28b789c202b744b45d49a77627c88f0c9b3d56c4b86747940af")
    version("0.9.28", sha256="8b589005fe04af6d0426830db299d66734be7541f92d8940204ad7fb615ec478")
    version("0.9.29", sha256="62f3078fb58855854437e14d5c52a7d440a11d258eaf21d018fa00a1630900bc")
    version("0.9.30", sha256="1f531cbcbef6e7ee001811feecc7f747feb2fe7b44b84ea07be1bc9c97f5807b")
    version("0.9.40", sha256="1685677243b402f3c6dbd729743da80dbdb9e035bf0be230d843556d64aa1678")
    version("0.9.42", sha256="c344f1487857e68a9104d8e4dea5eb481f5c1daee404c1fc1475fd695360342d")
    version("0.9.50", sha256="b570b68641467162f2a3a748bf50ac6b5a6888dbcc885a184c784dd8617cc62d")
    version("0.9.60", sha256="5d54950a1956c6faff3c82cd116aed4436cf0e322a72747d77b9189d5ec7f8cb")
    version("0.9.65", sha256="646d8fb2ca04858374da1b54e9818f88dc2b254deb0f74bf0f3911773e7eaf94")
    version("0.9.8", sha256="5808a66a070cc3b9f22a0fd4c4c953fa91f3f501238721d9b4bccc7cbc03f266")
    version("0.9.9", sha256="0b1511709d48153b10dc589b8a124d5b629574989c58b7951ee42d7408a7b816")

    depends_on("py-setuptools", type="build")


# {'requests(>=2.2.1)': ['0.10.0', '0.11.0', '0.12.0']}
