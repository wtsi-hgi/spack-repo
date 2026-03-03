# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyQnorm(PythonPackage):
    """Quantile normalization"""

    homepage = "https://github.com/Maarten-vd-Sande/qnorm"
    pypi = "qnorm/qnorm-0.8.1-py3-none-any.whl"

    version("0.0.1", sha256="7ec986e82ca97cb9b128c0aecdbcd35799f8c1ff87a15140ce7b77e5e37a46b7")
    version(
        "0.0.3",
        sha256="39d0e102835eaab277be40fb3342db6eae240ef69f226f6cf91cf8fc92dfd458",
        expand=False,
        url="https://files.pythonhosted.org/packages/49/df/aef281a451a69cef59157f6cd9a33d72d6c081ccde09747a81aa2d9d44d1/qnorm-0.0.3-py3-none-any.whl",
    )
    version(
        "0.0.4",
        sha256="38644f367c744ebae025ca200d2c73e82294b8a0384dd2bb673f95620668136d",
        expand=False,
        url="https://files.pythonhosted.org/packages/e5/54/f9ec7be0997244ff2853040597955edc9624090b0acc8b3b5b766acba277/qnorm-0.0.4-py3-none-any.whl",
    )
    version(
        "0.0.5",
        sha256="d924cf0d0f86efae072965f4b8fbd3919aa25272925d7a5c9b7ade0983f53fba",
        expand=False,
        url="https://files.pythonhosted.org/packages/f4/c3/064d3fd07f5d20bde422796c4dd8ba18d1ea7ac0401e6ff15b516d1d2320/qnorm-0.0.5-py3-none-any.whl",
    )
    version(
        "0.0.7",
        sha256="ca47faa97038927b69d6e8f61ef0645c6bae3092e10e9786d8457855725ed49e",
        expand=False,
        url="https://files.pythonhosted.org/packages/c4/53/76f323adcd869c21b5eb005174c6ae762d495bc6c5848a3c84b441729f85/qnorm-0.0.7-py3-none-any.whl",
    )
    version(
        "0.0.8",
        sha256="77a7c00b74bce311d3b07ea6ce9a108226d010853c8bc9683cea810e19749a82",
        expand=False,
        url="https://files.pythonhosted.org/packages/91/c4/076a373f480caebb1391b4df89161a81f4ae7eb79c5808d773a9aea38bbc/qnorm-0.0.8-py3-none-any.whl",
    )
    version(
        "0.1.0",
        sha256="9629b73d1c1a66b06ae8da9436870ddb5ae227db2dac8d314f23893eb74a6adc",
        expand=False,
        url="https://files.pythonhosted.org/packages/10/14/e9be9c2c3ed9d299438f4264ed3cb3b8ca61cfd6ed90fac94e4af15d2c1d/qnorm-0.1.0-py3-none-any.whl",
    )
    version(
        "0.1.1",
        sha256="a1ff57b0e2a7829a9d1e7682cb8da3c2c650fa8b3d6473dbdf12e55b1ab4adeb",
        expand=False,
        url="https://files.pythonhosted.org/packages/40/ce/d5aee4bebf768e0c031f46505a6016aceb0ee08d79acdd0428edf78ae115/qnorm-0.1.1-py3-none-any.whl",
    )
    version(
        "0.1.2",
        sha256="e92d0c44d1e879313effb2178c00c641dfe44bff799bb7a1586202497e409afb",
        expand=False,
        url="https://files.pythonhosted.org/packages/dd/81/8dfd5ffeac6ed25aecafa75fccfe4d12761e2b7eeedbfbbd95f2075cc433/qnorm-0.1.2-py3-none-any.whl",
    )
    version(
        "0.1.3",
        sha256="b8be50bd3ba372d06ba27d008e1f2db5075aee4a7965654d3a1b4bad864df397",
        expand=False,
        url="https://files.pythonhosted.org/packages/c7/a1/a0c0303210cfbaca803999964483f7b64793ada00750bc86b2c21f6f1c31/qnorm-0.1.3-py3-none-any.whl",
    )
    version(
        "0.2.0",
        sha256="9df49bb71ab551d4ec4e95465b52e688d6c96a5b0626cf2729f4523a6875ec19",
        expand=False,
        url="https://files.pythonhosted.org/packages/13/59/0d284207e9234e2445c81f43e3492c49215e158b0ad65bb81131fdaeeeef/qnorm-0.2.0-py3-none-any.whl",
    )
    version(
        "0.2.1",
        sha256="75494d5a2613f5ebc0982bc64208b8cefe30a16718a605c8d290ed3aed75063d",
        expand=False,
        url="https://files.pythonhosted.org/packages/27/3a/936c34a69d7b40f282e7e611083506f298d457d64d3d1afd50a537c25e50/qnorm-0.2.1-py3-none-any.whl",
    )
    version(
        "0.2.2",
        sha256="27152c1335b905a502cdd390fc8a13de340ac46d4a047684d48b34bf20eefa11",
        expand=False,
        url="https://files.pythonhosted.org/packages/b5/63/12a005c89687252918a4f1d82408ca7d2cbfd3cfaba8a3df932ea0748e77/qnorm-0.2.2-py3-none-any.whl",
    )
    version(
        "0.3.0",
        sha256="95875f3f4daa3d4897426176b9843ab095e758b6e29e0f122c620183845d8f6b",
        expand=False,
        url="https://files.pythonhosted.org/packages/79/b0/5326286174b9ab3158638e5b1a5f15a5ff70e6cd0faf58add0c88e793e74/qnorm-0.3.0-py3-none-any.whl",
    )
    version(
        "0.3.1",
        sha256="bda68f1e036bc4b188d0dec0115c13b06abf07fc6a820aff5952e9683ed4334e",
        expand=False,
        url="https://files.pythonhosted.org/packages/cc/c3/540cf5c7396840dfcdecba07ee48fa347733c3f8e6add0c24d2290a50457/qnorm-0.3.1-py3-none-any.whl",
    )
    version(
        "0.4.0",
        sha256="76b2630456baf06d4008defda05136d22b3b6ecae9ab92944187718666c47849",
        expand=False,
        url="https://files.pythonhosted.org/packages/fb/7a/6eb9d263379d614fbdf779b399eee4c0f59271473a1d967a09f6c0c4d52d/qnorm-0.4.0-py3-none-any.whl",
    )
    version(
        "0.5.0",
        sha256="16ea35eb915c19a5a05133a0de0c09cebfe69e52717a08c72e94ce3aa6338514",
        expand=False,
        url="https://files.pythonhosted.org/packages/ab/27/9860eb9a3f6851425cdcf8876bc0b33f8baa188bcb125fecc84e51ca0589/qnorm-0.5.0-py3-none-any.whl",
    )
    version(
        "0.5.1",
        sha256="277c8f300837badca4267665103874eb0d78e1a134dbe5fb1376924b7e730710",
        expand=False,
        url="https://files.pythonhosted.org/packages/9a/e0/3103e3f61c47eec94f598835a1ff21df46463482c077c36ed0e6da8c5593/qnorm-0.5.1-py3-none-any.whl",
    )
    version(
        "0.6.0",
        sha256="90ea5fc99fe9bd00d0d7803322de143d74aa40bccb5c94bf16a0682db3d03ef3",
        expand=False,
        url="https://files.pythonhosted.org/packages/19/e1/56c8faf4568be07fb8d390105b795f600555a70b7a54f570edd3a99d958f/qnorm-0.6.0-py3-none-any.whl",
    )
    version(
        "0.6.2",
        sha256="be75a5dacc075634f4f126fc46301d08aaf7ef010ac45d1325deb8d772f9dd52",
        expand=False,
        url="https://files.pythonhosted.org/packages/d8/b1/758de320a1ccfb8d2ef28f23c40c034fd9a60adf0ce5e2f12876125ee855/qnorm-0.6.2-py3-none-any.whl",
    )
    version(
        "0.7.0",
        sha256="1faa3d3c79f1532c6c4c900214d48b3953844ab7cf0cae388450b97584c789e3",
        expand=False,
        url="https://files.pythonhosted.org/packages/6a/71/395432ab456505d41adafdd16cead5900c2289a975b38cb06e79bd18b0b2/qnorm-0.7.0-py3-none-any.whl",
    )
    version(
        "0.8.0",
        sha256="bed17f5bf76df9be75d1315e31f6874ffbd360195caa230f1d5c543fde66bc3d",
        expand=False,
        url="https://files.pythonhosted.org/packages/56/5b/416aff48b575994c3edec5fae557912884ccdc17bede3afebb7902c3c0b2/qnorm-0.8.0-py3-none-any.whl",
    )
    version(
        "0.8.1",
        sha256="9d6ce4e82444155922baf06aa89f9f939b54f53844e340bf2c6d9e7ff8821c41",
        expand=False,
        url="https://files.pythonhosted.org/packages/45/bc/80350513f3abf14f6dd921bf083f241ebc826c94556931c51f05348fd442/qnorm-0.8.1-py3-none-any.whl",
    )

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))


# {'numba': ['0.0.3', '0.0.4', '0.0.5', '0.0.7', '0.0.8', '0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.2.0', '0.2.1', '0.2.2', '0.3.0', '0.3.1', '0.4.0', '0.5.0', '0.5.1', '0.6.0', '0.6.2', '0.7.0', '0.8.0', '0.8.1'], 'numpy': ['0.0.3', '0.0.4', '0.0.5', '0.0.7', '0.0.8', '0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.2.0', '0.2.1', '0.2.2', '0.3.0', '0.3.1', '0.4.0', '0.5.0', '0.5.1', '0.6.0', '0.6.2', '0.7.0', '0.8.0', '0.8.1'], 'pandas': ['0.0.3', '0.0.4', '0.0.5', '0.0.7', '0.0.8', '0.1.0', '0.1.1', '0.1.2', '0.1.3']}
