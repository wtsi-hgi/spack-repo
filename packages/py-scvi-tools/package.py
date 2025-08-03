# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScviTools(PythonPackage):
    """Deep probabilistic analysis of single-cell omics data."""

    homepage = "http://scvi-tools.org/"
    pypi = "scvi-tools/scvi_tools-1.1.2-py3-none-any.whl"

    version(
        "0.10.0",
        sha256="f3d13de9656a5105febb16f06e8ac07986907c41700fe9b0a77f9f28cd456808",
        expand=False,
        url="https://files.pythonhosted.org/packages/69/22/0a0d44f417a7c3f14f35b0e88813d3c8646401d5d6dfb1434b9451303a22/scvi_tools-0.10.0-py3-none-any.whl",
    )
    version(
        "0.10.1",
        sha256="2bf95eb25704053cc75dc0830cbd9354ab2c09f6e0a7d6f38cb94d6751fc5115",
        expand=False,
        url="https://files.pythonhosted.org/packages/74/7a/5d6011c3c01a806bb49bddd041427667296163ef17880b98ca2e73909359/scvi_tools-0.10.1-py3-none-any.whl",
    )
    version(
        "0.11.0",
        sha256="806bac8cede7731d056ac1ac769d578a64245915c6ea70c2b2ae04fa0cc4af3b",
        expand=False,
        url="https://files.pythonhosted.org/packages/0d/38/82c6aaa2338a14d7e80fa32044c31f46eadfdddfe4e09a331a0a0d3db9f1/scvi_tools-0.11.0-py3-none-any.whl",
    )
    version(
        "0.12.0",
        sha256="cf5c3c3ca07c5a3af1a2b1a96b30fa7c22c7944285204fef5eb3fbcc922994d9",
        expand=False,
        url="https://files.pythonhosted.org/packages/b9/fa/87108a5afcd34a6e70e785b3298e49f40e0ddbd775bb84f2fa67cb9955f8/scvi_tools-0.12.0-py3-none-any.whl",
    )
    version(
        "0.12.1",
        sha256="e8bf2b2150f3c07f2cd7ed6318bfca0ebe7ab57b38f05dde91a3d7bfaac1142b",
        expand=False,
        url="https://files.pythonhosted.org/packages/15/df/f450d282148f2ad7090229bb9d22c5873945517c990e2f627b45fe088c6e/scvi_tools-0.12.1-py3-none-any.whl",
    )
    version(
        "0.12.2",
        sha256="8f7f95e6405e98e9dcf4db3009243199fc57daf22a3c2160f1d010f352eefca0",
        expand=False,
        url="https://files.pythonhosted.org/packages/0b/b7/654a2eab9ea853b61d6b06bca402ac58150871f464783f2f5ecf6cbdd2a6/scvi_tools-0.12.2-py3-none-any.whl",
    )
    version(
        "0.13.0",
        sha256="2958af3d46c8db0b2ca71c1d65ce4ada4c588f72a789d32707446fe4d2074d86",
        expand=False,
        url="https://files.pythonhosted.org/packages/8d/07/37f4470ab72f28dcbfea63014dc47519cf6645e3ec83c4da8255fc6cea64/scvi_tools-0.13.0-py3-none-any.whl",
    )
    version(
        "0.14.0",
        sha256="fb458e633d3a96f846214ffc4051824d10aec6f3fb354ef1f2540aaca793968a",
        expand=False,
        url="https://files.pythonhosted.org/packages/42/be/7056fae9df9abd372a4378380c968d655f78b7e4f8714de6701b98876904/scvi_tools-0.14.0-py3-none-any.whl",
    )
    version(
        "0.14.1",
        sha256="976c89d8e5c281f5f9ef4ba55b9bbcbc1856b1ca5cb13bc1426f4fc6e895b618",
        expand=False,
        url="https://files.pythonhosted.org/packages/4b/13/645e7a3612daf5ef67ee27089efc6ceece9c0daac89252aaebc9e9e307ad/scvi_tools-0.14.1-py3-none-any.whl",
    )
    version(
        "0.14.2",
        sha256="54d952bda064078d0b7b80fe5424b686e15855b91a9f98aeb784dece24dee6cf",
        expand=False,
        url="https://files.pythonhosted.org/packages/69/cd/ed807de211079f7db9f1caa246a64f74eea212ea35bf0e177548387049da/scvi_tools-0.14.2-py3-none-any.whl",
    )
    version(
        "0.14.3",
        sha256="ab48e0c3b8146dae828a2a722ae1d8d98fdc1ee26f1a287e43d939be197ccd6e",
        expand=False,
        url="https://files.pythonhosted.org/packages/3e/52/c8182a5d84e2cb2650197dddcaeed88d7b6633422858b1f70fe9d1846635/scvi_tools-0.14.3-py3-none-any.whl",
    )
    version(
        "0.14.4",
        sha256="a0d22fcd4cccc68f988e7bb2400dbeabbd0e10f98aff51c2a2c13edc1c968e5e",
        expand=False,
        url="https://files.pythonhosted.org/packages/52/d3/a05c169504d63461527381a36d7dbf7ec6fe98474c8b272e6a83e22e9572/scvi_tools-0.14.4-py3-none-any.whl",
    )
    version(
        "0.14.5",
        sha256="c584c2d86f9d1491960eae996c8c34f260225d7f69d6e9ea917aa12d1494d609",
        expand=False,
        url="https://files.pythonhosted.org/packages/fb/96/42709ca106201cf0948874ddf8640954245ab22d56f4076f1ce555b3e335/scvi_tools-0.14.5-py3-none-any.whl",
    )
    version(
        "0.14.6",
        sha256="ce36d15476d022f4ffde6d5227f417b36bb38db69134d4ca63c20733a960316c",
        expand=False,
        url="https://files.pythonhosted.org/packages/b3/8d/872d4983931ae6eb7bb9319277d6d92daf51b3d4aad5b9a772ba7bc6600b/scvi_tools-0.14.6-py3-none-any.whl",
    )
    version(
        "0.15.0",
        sha256="68644b9a01f411f67434f6f14fd19e0f0e4f972908dd48dd966fc1cc3a555a22",
        expand=False,
        url="https://files.pythonhosted.org/packages/69/b8/b39d240497f556ef0713ea6fb2628d539ff18dd9e8cc46b95876bdfbf67b/scvi_tools-0.15.0-py3-none-any.whl",
    )
    version(
        "0.15.0a0",
        sha256="e59da1a817962de56c6852425c35a28d2efc132b0a1dcbd69702e4af525b795f",
        expand=False,
        url="https://files.pythonhosted.org/packages/9a/be/1c62603767e375cdc38b02b670f02a73745d65532bb078f87a84b0a9985c/scvi_tools-0.15.0a0-py3-none-any.whl",
    )
    version(
        "0.15.0b0",
        sha256="30d60d890e83f0215d23ed775789537c213a32221ce22544f2651a39e0e378b7",
        expand=False,
        url="https://files.pythonhosted.org/packages/e0/fe/4400640f1a520565cdf347d1cd8b7b01b914cd62978d17a0b66474283f64/scvi_tools-0.15.0b0-py3-none-any.whl",
    )
    version(
        "0.15.1",
        sha256="f5951275f3198a6511e62c204daaf96c6b9851c327187c45a1ea3e93935c4978",
        expand=False,
        url="https://files.pythonhosted.org/packages/7e/22/a21de2f3f092217541e481b16744fc8a90ea022a4fb742ac273a79d6bd3e/scvi_tools-0.15.1-py3-none-any.whl",
    )
    version(
        "0.15.2",
        sha256="bb1341db15f481bb43d66a39c6d9b1b8b0bb837b7e0db7fd58f022a65df6c3e8",
        expand=False,
        url="https://files.pythonhosted.org/packages/96/9a/9009146153a977e6aff76621ee388cf39bfd991cb33d71a611870575145c/scvi_tools-0.15.2-py3-none-any.whl",
    )
    version(
        "0.15.3",
        sha256="207bccf130bb03261939e7ae8a2dfee09c2a27ded1c6977013229e3535d58d4e",
        expand=False,
        url="https://files.pythonhosted.org/packages/50/03/32533725297197792ba5d2779139e94285f0ec92a22f7433a5bc06b5edfc/scvi_tools-0.15.3-py3-none-any.whl",
    )
    version(
        "0.15.4",
        sha256="7ca8dec65c122590404e615a0e477e48c4d6295b319afec2b83e4fd1ab8a064e",
        expand=False,
        url="https://files.pythonhosted.org/packages/48/23/20be78b99074e9e5f982d56469fbd11d6775bd561ee0589314df1412229b/scvi_tools-0.15.4-py3-none-any.whl",
    )
    version(
        "0.15.5",
        sha256="a1991261557c7c6cfa3b7d2d777b71edfbcb66682f163364f1940f9c6d33fd9b",
        expand=False,
        url="https://files.pythonhosted.org/packages/72/f9/7ff279ec01dce3150e25f21dc70b123dd60be2afa72dc076a64aedf6d32a/scvi_tools-0.15.5-py3-none-any.whl",
    )
    version(
        "0.16.0",
        sha256="cec6fd9829b1a7a2c1e683e00f069be35fad6a708296c4d04cdd51eceaf728fc",
        expand=False,
        url="https://files.pythonhosted.org/packages/5f/6a/18af14643c102c3c63c139eae608e6d251a96f506c3d17153f70cb713f07/scvi_tools-0.16.0-py3-none-any.whl",
    )
    version(
        "0.16.1",
        sha256="0edb73285f438e0da24a0c3638b36c4bb89b31cc111fbe65d2b6c63b6f88f545",
        expand=False,
        url="https://files.pythonhosted.org/packages/de/c1/1da80b3276f580a16dc87d05a65877b940eef1266e3226c43476c441f36f/scvi_tools-0.16.1-py3-none-any.whl",
    )
    version("0.16.3", sha256="0323d99e7d76e45605747a7457b8658d2a39a28d984136a3b970821a03eb1654", expand=False)
    version(
        "0.16.4",
        sha256="d5cd27cb05e9e930fab78758ff5032fd2bb9489cdceaf9023ad0e5708f49318b",
        expand=False,
        url="https://files.pythonhosted.org/packages/7a/78/1cafc39f3adcc649489bdb35b825f566baedc8dbab2d5f0aea2ae3a8c4c5/scvi_tools-0.16.4-py3-none-any.whl",
    )
    version(
        "0.17.0",
        sha256="9f83e7fb628f9f96ee446a47b257a433f9e98c35e258e324f0c224ee1533ab74",
        expand=False,
        url="https://files.pythonhosted.org/packages/8d/8d/cfe014c42061dd88be6995cfa040e12342632eecc1570c0974af409a97ce/scvi_tools-0.17.0-py3-none-any.whl",
    )
    version(
        "0.17.0b0",
        sha256="b1c1d3a3bcfbd65745e08686aed66f0b54d9364dc2a30525852e822ce813497f",
        expand=False,
        url="https://files.pythonhosted.org/packages/64/37/eb669124bdc433443658357deeec43f56811f48c6030dab0a46c302d9444/scvi_tools-0.17.0b0-py3-none-any.whl",
    )
    version(
        "0.17.1",
        sha256="0328bf1dae34210c23029c8ae5eac6c2b3bb25adc4ed541b79e668d125cbfc60",
        expand=False,
        url="https://files.pythonhosted.org/packages/5e/34/602e8573f04c92669e71d03744e4d9fa13ba2df8c7b3b8ad5e824dd1023b/scvi_tools-0.17.1-py3-none-any.whl",
    )
    version(
        "0.17.2",
        sha256="7f748874182a66eaf08cc0da1340d747cd09a24d388815cef0631a31541f2cfd",
        expand=False,
        url="https://files.pythonhosted.org/packages/bb/34/1b19a7cfc47f0a9c78e572483ce607ae13529294562e4bc0449c9386ce98/scvi_tools-0.17.2-py3-none-any.whl",
    )
    version(
        "0.17.3",
        sha256="513de9fa32b2ad01408528a1bf0d29a55a84ea10920ed0401af75ba709651131",
        expand=False,
        url="https://files.pythonhosted.org/packages/dc/39/d58957c3fef341d0fcfefe212dc473e61b7054c2549b6f67542693980801/scvi_tools-0.17.3-py3-none-any.whl",
    )
    version(
        "0.17.4",
        sha256="594beaefd3fcb385462b3f55a5a9ace1c74c58a235495fbcdd144c3bb6cb1f50",
        expand=False,
        url="https://files.pythonhosted.org/packages/52/e9/9ad87f9a658ca6f0103e13a5e024a424fc2c3dd1cca6f2213a000b1aad17/scvi_tools-0.17.4-py3-none-any.whl",
    )
    version(
        "0.18.0",
        sha256="0849cc0e728cec7b4591cd6abdafc56039a5b29de389d24b4264331c6add08ff",
        expand=False,
        url="https://files.pythonhosted.org/packages/3d/bd/033dce08648104bc87212cff9fe93d096baa3433fffb6b4407d36a3d53ea/scvi_tools-0.18.0-py3-none-any.whl",
    )
    version(
        "0.19.0",
        sha256="951abf0a11c2082c9e8fdc09a60de7449ce4168e7d1608c4568f85cf71e16b1d",
        expand=False,
        url="https://files.pythonhosted.org/packages/e0/52/96e75badf5e23508d3e3e3ca5084f224c59794c6e119993419761de040f5/scvi_tools-0.19.0-py3-none-any.whl",
    )
    version(
        "0.19.0a0",
        sha256="e203e5d8548b5c415d3f46700c8faaeff13e8f62e20861f7be37401127611756",
        expand=False,
        url="https://files.pythonhosted.org/packages/3c/37/d6e9a583f513b034e3a0f2653f80c5a81a7e054b3406b21bc8d210734a44/scvi_tools-0.19.0a0-py3-none-any.whl",
    )
    version(
        "0.20.0",
        sha256="ab274c73a70eecc688e6925c0167e53ac155cb1860ff871577eff5d8f712ab24",
        expand=False,
        url="https://files.pythonhosted.org/packages/98/03/bfb1a378fe3be32d8e8f2459e888c0604c2041b1ca3730765ef7f1b3141e/scvi_tools-0.20.0-py3-none-any.whl",
    )
    version(
        "0.20.0a0",
        sha256="cce99d24b721ef6a4cd752c0f9bb761039120a3ae7b50422003a52efae729658",
        expand=False,
        url="https://files.pythonhosted.org/packages/cb/76/6c6bea2b72f887c2877133bae06828835ee57b8a473da59cc7443e835af9/scvi_tools-0.20.0a0-py3-none-any.whl",
    )
    version(
        "0.20.0b0",
        sha256="916000482bddbbb30b96a66cc8ce5ffe8148d5da37ab7622450a59799395664e",
        expand=False,
        url="https://files.pythonhosted.org/packages/ba/a8/d696125ec623b29f049bc1bcec6f5f0965962af3209ef5a7474f7cf96203/scvi_tools-0.20.0b0-py3-none-any.whl",
    )
    version(
        "0.20.0b1",
        sha256="87f9d05758e1076529dde8e288609a9cfc89000d517b45e8b9cc61767b893947",
        expand=False,
        url="https://files.pythonhosted.org/packages/c7/d8/7e07867f2bf08e3705f58ec3675b810fde35f7e787a5f2ac7b31812c0666/scvi_tools-0.20.0b1-py3-none-any.whl",
    )
    version(
        "0.20.0b2",
        sha256="cbed16132788a3c51431640d01925abb234aefc4e433c7136e0d492e204d228c",
        expand=False,
        url="https://files.pythonhosted.org/packages/4e/f8/cd6c09c260aa16819f59b7dd6538435093090df544ab36087ff07bd984b6/scvi_tools-0.20.0b2-py3-none-any.whl",
    )
    version(
        "0.20.1",
        sha256="704b0fc6b944930965e0259abb22b3a21a912ac82ebc6c70d9f1bd305f007588",
        expand=False,
        url="https://files.pythonhosted.org/packages/d4/4e/6dc47fa9e3ccda23720da5723bfa278220a88ed72d86903b54a936f84291/scvi_tools-0.20.1-py3-none-any.whl",
    )
    version(
        "0.20.2",
        sha256="368a7767c4b35548c72387cb2c97ef759be9b157cba582f825e31ded812aa27f",
        expand=False,
        url="https://files.pythonhosted.org/packages/2d/87/96b8ce90489089a29a91e632de6ffb600d363f17929a2a61fe57564b0e8a/scvi_tools-0.20.2-py3-none-any.whl",
    )
    version(
        "0.20.3",
        sha256="9e02c1d7770a56300569def2c48b4d99cb92f9ca5dcce9d2cb19d463d2aafed5",
        expand=False,
        url="https://files.pythonhosted.org/packages/c0/f2/aeb400729cc727d889f3ced11971b22ffab105acc3586411cc256c897d27/scvi_tools-0.20.3-py3-none-any.whl",
    )
    version(
        "0.7.0",
        sha256="23470e09f8c43e3f9e20216aa9b3d007bfe2ff84891ef0f0686795b7776f1163",
        expand=False,
        url="https://files.pythonhosted.org/packages/90/bf/1ef4ee55a1a0f7b20ea440f338c298c8aa12408c37d843e9e9229a7de15d/scvi_tools-0.7.0-py3-none-any.whl",
    )
    version(
        "0.7.0a0",
        sha256="1cac5ae4fbcfe7757b13c92a04db071a641d52d609148cb7290845986f42166e",
        expand=False,
        url="https://files.pythonhosted.org/packages/e2/a9/c3146c91ad4db627c66cae2be5aedb62e806ca6f10d041ba5d30d0ad6e9f/scvi_tools-0.7.0a0-py3-none-any.whl",
    )
    version(
        "0.7.0a1",
        sha256="432352b4ab450f171056f1a44cc5d4e7ba9e8510e998ba5bcd663eb9c31a179c",
        expand=False,
        url="https://files.pythonhosted.org/packages/42/f2/00d1519f9c469ddfb33f88fecacf95ad37c19c230965691b31adb6c33204/scvi_tools-0.7.0a1-py3-none-any.whl",
    )
    version(
        "0.7.0a2",
        sha256="0995a5db093e639b802783fdc5220f3993c7bc25191bc3a0a582553c81075b5e",
        expand=False,
        url="https://files.pythonhosted.org/packages/18/25/3cf155f144fafd330cf408a6b3c86904e69829b9fac5cad1021579122217/scvi_tools-0.7.0a2-py3-none-any.whl",
    )
    version(
        "0.7.0a3",
        sha256="218eec643b6a971b1262de7004fba2215bab8cb4cc1a4f9f039bc39fab1d05ab",
        expand=False,
        url="https://files.pythonhosted.org/packages/03/9d/c1781d6a53fa5b3fdcb5fae80113babe5f27db42de28db97282369de3c09/scvi_tools-0.7.0a3-py3-none-any.whl",
    )
    version(
        "0.7.0a4",
        sha256="bd28f3758ba804d355fa942a4a340c2253048bdeb58ae7acffe97bcb2ae2859f",
        expand=False,
        url="https://files.pythonhosted.org/packages/d5/ce/33c5e5a7df8082cad49bf15ebb64361971eabfdc6c2d6d720f87bee87b38/scvi_tools-0.7.0a4-py3-none-any.whl",
    )
    version(
        "0.7.0a5",
        sha256="ec6476bc0b55906f206cb406c6ea7264133a043b3637516c365816e5ce5b718f",
        expand=False,
        url="https://files.pythonhosted.org/packages/82/15/c871c25d920414bd17f29c46e5a7a6454fd6f2e6726a5cf5e0c935aaa5fc/scvi_tools-0.7.0a5-py3-none-any.whl",
    )
    version(
        "0.7.0a6",
        sha256="3a74c0a840f867ede27672884e2d3d387fd4ed3faf1e2a9489a2808661fd361e",
        expand=False,
        url="https://files.pythonhosted.org/packages/86/04/454d4e7ee3e4a0eb471a8460836a5d8a33bc42f9a529f22603dc037047b8/scvi_tools-0.7.0a6-py3-none-any.whl",
    )
    version(
        "0.7.0b0",
        sha256="e91ec568d4a9dc9ca1cc557c6079fcdc977d55b66699a310b5b88539f0355cc6",
        expand=False,
        url="https://files.pythonhosted.org/packages/3f/e5/313aacd14ba8188422f19776a2399f0da4abea6c4c6fae15f3efece83085/scvi_tools-0.7.0b0-py3-none-any.whl",
    )
    version(
        "0.7.1",
        sha256="f5a4df6d602353128e8f26d9b993b261ae3d310a8875c0ad20e23cd805f384fa",
        expand=False,
        url="https://files.pythonhosted.org/packages/ce/1d/4b04b6f350d75cca6fa47cd27c6cddd6ec945becf4db1e918f2b561a45cd/scvi_tools-0.7.1-py3-none-any.whl",
    )
    version(
        "0.8.0",
        sha256="12162a29fba937e2738ad28b72ff4ae982d9b8abfae35879ab984b29adca995e",
        expand=False,
        url="https://files.pythonhosted.org/packages/84/57/f5977a095e58b9d209e3147291716b39c3e893d485489c3bf26eeb655fdf/scvi_tools-0.8.0-py3-none-any.whl",
    )
    version(
        "0.8.0b0",
        sha256="71d23f549a818cbfba99daea30b631cd8f91316eb413f4d5301f987b4758e975",
        expand=False,
        url="https://files.pythonhosted.org/packages/f1/8f/cf34b8d7956eb92b32e9cdf465a72fa0dbf4753e09a9a7b1c6c8354f0021/scvi_tools-0.8.0b0-py3-none-any.whl",
    )
    version(
        "0.8.1",
        sha256="299e5a889c7eb87af6021aa3b6aeb97d26552c2f3988a7ea81b5d26277557221",
        expand=False,
        url="https://files.pythonhosted.org/packages/82/fb/c7094dc71ff68c50ea233767302ca61f05f81a943935b616cad38476d900/scvi_tools-0.8.1-py3-none-any.whl",
    )
    version(
        "0.9.0",
        sha256="45ef6378dfd98833f31105fd098d2c902b25a051f1d3ef29e4919909b971c161",
        expand=False,
        url="https://files.pythonhosted.org/packages/bc/30/f03401c403cb98d13e5fc6d52b88a15a6b10581bc3ea0f0daab18538dfa2/scvi_tools-0.9.0-py3-none-any.whl",
    )
    version(
        "0.9.0a0",
        sha256="e60a3f550d238008b53698c5460aa9778bcffc5c3f2001ae999ad788ed94a5ee",
        expand=False,
        url="https://files.pythonhosted.org/packages/15/25/d938ba21ce50b09b70f79cc83b2aacca2cc09a90b7ff5b2a01a2e19f8708/scvi_tools-0.9.0a0-py3-none-any.whl",
    )
    version(
        "0.9.0a1",
        sha256="49f03b5da2f1ec440ffc8d6d867bd6a0453c4e3080f95297d1fd3f6ad4dabc9c",
        expand=False,
        url="https://files.pythonhosted.org/packages/77/27/347eb15ebfdc0830f513eb49c9b45249b4ec41ca54ef0f4fbd80edbf8d23/scvi_tools-0.9.0a1-py3-none-any.whl",
    )
    version(
        "0.9.0a2",
        sha256="7aedba45beff222abbd8dc60d1fa7b1e949959114b6486e2830e4da9e4ac9098",
        expand=False,
        url="https://files.pythonhosted.org/packages/99/8c/5feec4dd2f0855e5ea3dd3bb65a731adf315dbf61eb5dd29389ff790b42b/scvi_tools-0.9.0a2-py3-none-any.whl",
    )
    version(
        "0.9.0b0",
        sha256="c784e2544bb8af946c9577b71eedddb5a8afc3cc670f4da1dc05682d38aa88ea",
        expand=False,
        url="https://files.pythonhosted.org/packages/3e/4b/3f207e103ea26312f3c2ae22e81ec53db4478b49b5961b9167a5c87af7f6/scvi_tools-0.9.0b0-py3-none-any.whl",
    )
    version(
        "0.9.0b1",
        sha256="f5025287707abb7d13e11ff12085bef24794011f34c4ba8c6cd0acffb40cc22f",
        expand=False,
        url="https://files.pythonhosted.org/packages/71/d5/cc19b0de72bf79c1619e122a9aac545093399c11ff422bb7dd8851023667/scvi_tools-0.9.0b1-py3-none-any.whl",
    )
    version(
        "0.9.1",
        sha256="b114b4863673a94fb10c78a0d51704381d0d65bc2eecc24353fcf2e1e5637a28",
        expand=False,
        url="https://files.pythonhosted.org/packages/70/87/2313e36887d592e68f4dd07bf65dcf46c0855e6a33723bca275914a2731a/scvi_tools-0.9.1-py3-none-any.whl",
    )
    version(
        "1.0.0",
        sha256="08151167a303b360f036553f6c625ad6493a33b7fc5731ff97a2312375fbc12b",
        expand=False,
        url="https://files.pythonhosted.org/packages/bd/90/b5b99d3b5c05a7b791b6067d430a1b62088a66f08508c704224ebc9c3487/scvi_tools-1.0.0-py3-none-any.whl",
    )
    version(
        "1.0.0b0",
        sha256="b1a120819b1ffbbc7886091258dff69dcb31b9a48867e28d46b499487638fe23",
        expand=False,
        url="https://files.pythonhosted.org/packages/1c/9d/ba19f07afcaa78308d2464358e45b70d3fd8ce25cc7bbcb07e2df6fd5ca0/scvi_tools-1.0.0b0-py3-none-any.whl",
    )
    version(
        "1.0.1",
        sha256="4cec47e47233d5975a70be065c7207e991fd30ff849fa5caef87db90961e07d2",
        expand=False,
        url="https://files.pythonhosted.org/packages/75/66/5b8763194a466fb55cd8539a56945a94a27320bf195b580f641157ff7f74/scvi_tools-1.0.1-py3-none-any.whl",
    )
    version(
        "1.0.2",
        sha256="1549ac4b4430a03c5c8eea3488e3c846fce9f8aedbb01aef5cf948ecdad5f9d6",
        expand=False,
        url="https://files.pythonhosted.org/packages/ce/7d/13ef7fc775387b588268b210bde63c59d546bd7ed263214b6a9fecf4a1da/scvi_tools-1.0.2-py3-none-any.whl",
    )
    version(
        "1.0.3",
        sha256="b435c81fa2d2d65e212b7e12f62806584533e6754e62a4c5e27e69f669f5348d",
        expand=False,
        url="https://files.pythonhosted.org/packages/44/7a/02fcfcfb8cc9c24da800cc53f127deb5626989da44038b8af58facbb6dfb/scvi_tools-1.0.3-py3-none-any.whl",
    )
    version(
        "1.0.4",
        sha256="d445dc6a1304bee660c5abd2b5788d7211dcc610b23ca21afeec3a8b92a9b75c",
        expand=False,
        url="https://files.pythonhosted.org/packages/b7/79/c9e22e42b0a6d6b65e3291851641783379b04f541054ea1eed8486f57aa1/scvi_tools-1.0.4-py3-none-any.whl",
    )
    version(
        "1.1.0.post1",
        sha256="e488a581b9e3c9c02df712df96cf31d997e7be309ade49c0cf2fd7f02227486f",
        expand=False,
        url="https://files.pythonhosted.org/packages/ba/b5/d123f068ada10de7e97c1fc34eeb6cc807498dbb45f7170a568f07b40bde/scvi_tools-1.1.0.post1-py3-none-any.whl",
    )
    version(
        "1.1.0.post2",
        sha256="e8430af9b6210b050a0f78df88ea0a8476517ce2d5bbf27d4e2c98bb11bd75fe",
        expand=False,
        url="https://files.pythonhosted.org/packages/f0/5f/9ba49ed85d0dbd643fd02e83a87ae79ce0cf50e8570435ef9e2497469427/scvi_tools-1.1.0.post2-py3-none-any.whl",
    )
    version(
        "1.1.0rc1",
        sha256="b30f3b2a1ac7fd1f39579651c0056b2284fb424e2dd827df2a761136c48df51f",
        expand=False,
        url="https://files.pythonhosted.org/packages/f2/1d/7bdfb2fefdea4f9813ad87a9c50eb2bafa72ae8cd42f9559f6a20cd443de/scvi_tools-1.1.0rc1-py3-none-any.whl",
    )
    version(
        "1.1.0rc2",
        sha256="1597f93d815b4866ca8a18fcf695bffaf7ebba8029bc1f660fc135ca48393780",
        expand=False,
        url="https://files.pythonhosted.org/packages/31/91/d782f7134c67aecbd7dfe7cd5dbfd512ff2ba454b940291128d553bd6c41/scvi_tools-1.1.0rc2-py3-none-any.whl",
    )
    version(
        "1.1.1",
        sha256="281946fd0bc8bf9be748007950b2a4d4331ef473f515d3ccacf72ab866e461d1",
        expand=False,
        url="https://files.pythonhosted.org/packages/f7/f2/6fc4bc304156fded292296fd6418166a7f3459021e68caf1c6f68a380388/scvi_tools-1.1.1-py3-none-any.whl",
    )
    version(
        "1.1.2",
        sha256="c4b449cc162a497794c7965a6ec63467af06f50ad5a04aa78c1b04b8bed5ff04",
        expand=False,
        url="https://files.pythonhosted.org/packages/92/71/615517cd2048885bfa79324dbbc67aead4fbcf231f561ed616bca6bf9ec9/scvi_tools-1.1.2-py3-none-any.whl",
    )
    version("1.2.2", sha256="6e2295bbb8556cd440b2e0392686221b27f8171dba6c85af3d5d89e0a14061cd", expand=False)
    version("1.2.1", sha256="22348c8fc9e3febe7889ab2560977e658a65acae72a8f599f6347907ceb57acb", expand=False)
    version("1.2.0", sha256="3e56d15e426ad7e347fba95d4fe4d66b1b1a277e081cf94cfca82462589b4b23", expand=False)
    version("1.1.6", sha256="3059a7fa0aba63c6a29c7765ff30c473d2ecb353bf0c889a57b4e9fbebdd9cd9", expand=False)
    version("1.1.5", sha256="7d97f0ecad13656be6d39a6669937cee31b5c4506f872846bbb2771bfa00419e", expand=False)
    version("1.1.4", sha256="9db228589458c6f0fe939c3524b775123e4c60bcf9c9aa20211629193b47263f", expand=False)
    version("1.3.2", sha256="0125ee90ea27056df764bac4237df6723a5f25202c4ca28da1bb3a40e830d52e", expand=False)
    version("1.3.1.post1", sha256="3f72366ac6f6f2774a3360608d773f203ee01ace65a41944e204f48dbea697de", expand=False)
    version("1.3.1", sha256="c9e20d7b01305cedbbbf7b951d4305613f65c92f3a2278c82c4f5a6e693ef2b5", expand=False)
    version("1.3.0", sha256="0e401e263afea0a868337e361e15039a59d1e6fcb9707a03b66e56608ee5412e", expand=False)


    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-torchmetrics", type=("build", "run"))
    depends_on("py-torch@2.2:+cuda cuda_arch=70,72,75,80,86,87,89,90")
    depends_on("py-scipy@:1.10", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-rich", type=("build", "run"))
    depends_on("py-pyro-ppl", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-optax", type=("build", "run"))
    depends_on("py-numpyro", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-mudata", type=("build", "run"))
    depends_on("py-ml-collections", type=("build", "run"))
    depends_on("py-lightning", type=("build", "run"))
    depends_on("py-jaxlib", type=("build", "run"))
    depends_on("py-jax", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-flax", type=("build", "run"))
    depends_on("py-docrep", type=("build", "run"))
    depends_on("py-anndata@0.8.0:0.10", type=("build", "run"), when="@0.20:")
    depends_on("py-anndata@0.11:", type=("build", "run"), when="@1:")
    depends_on("py-sparse@0.14.0:", type=("build", "run"), when="@1.0.0:")
    depends_on("py-pytorch-lightning@1.9.0:1.10.0", type=("build", "run"), when="@0.20:")
    depends_on("py-pytorch-lightning@1.6.0:1.8", type=("build", "run"), when="@0.18.0:0.19")
    depends_on("py-pytorch-lightning@1.5.0:1.6", type=("build", "run"), when="@0.15.0:0.16")
    depends_on("py-pytorch-lightning@1.3:1.4", type=("build", "run"), when="@0.12.1:0.14")
    depends_on("py-pytorch-lightning@1.2:", type=("build", "run"), when="@:0.12.0")

    def setup_run_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", "/opt/view/lib64")


# {'anndata(>=0.7.5)': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'black(>=20.8b1);extra=="dev"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'codecov(>=2.0.8);extra=="dev"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'flake8(>=3.7.7);extra=="dev"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'h5py(>=2.9.0)': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'importlib-metadata(>=1.0,<2.0);python_version<"3.8"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.7.0', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'ipython(>=7.20);(python_version>="3.7")and(extra=="docs")': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.9.0', '0.9.0b0', '0.9.0b1', '0.9.1'], 'ipywidgets': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'isort(>=5.7);extra=="dev"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.9.0', '0.9.0b0', '0.9.0b1', '0.9.1'], 'jupyter(>=1.0);extra=="dev"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'leidenalg;extra=="tutorials"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'loompy(>=3.0.6);extra=="dev"orextra=="tutorials"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'nbconvert(>=5.4.0);extra=="dev"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'nbformat(>=4.4.0);extra=="dev"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'nbsphinx-link;extra=="docs"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'nbsphinx;extra=="docs"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'numba(>=0.41.0)': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0a0', '0.15.0b0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'numpy(>=1.17.0)': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'openpyxl(>=3.0)': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.8.0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'pandas(>=1.0)': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'pre-commit(>=2.7.1);extra=="dev"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'pydata-sphinx-theme(>=0.4.3);extra=="docs"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0a0', '0.9.0', '0.9.1'], 'pyro-ppl(>=1.5.0)': ['0.10.0', '0.10.1', '0.9.1'], 'pytest(>=4.4);extra=="dev"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'python-igraph;extra=="tutorials"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'pytorch-lightning(>=1.2)': ['0.10.0', '0.9.0', '0.9.0b0', '0.9.0b1', '0.9.1'], 'rich(>=9.1.0)': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.9.0', '0.9.0b0', '0.9.0b1', '0.9.1'], 'scanpy(>=1.6);extra=="dev"orextra=="tutorials"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'scanpydoc(>=0.5);extra=="docs"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'scikit-learn(>=0.21.2)': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'scikit-misc(>=0.1.3);extra=="tutorials"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'sphinx(>=3.4);extra=="docs"': ['0.10.0', '0.10.1', '0.11.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0a0', '0.9.0', '0.9.0b0', '0.9.0b1', '0.9.1'], 'sphinx-autodoc-typehints;extra=="docs"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'sphinx-gallery(>0.6);extra=="docs"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.9.0', '0.9.0b0', '0.9.0b1', '0.9.1'], 'sphinx-tabs;extra=="docs"': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0a0', '0.9.1'], 'sphinx_copybutton;extra=="docs"': ['0.10.0', '0.10.1', '0.11.0', '0.9.0', '0.9.0b0', '0.9.0b1', '0.9.1'], 'torch(>=1.7.1)': ['0.10.0', '0.10.1', '0.9.0', '0.9.0b0', '0.9.0b1', '0.9.1'], 'tqdm(>=4.56.0)': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.9.0', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'typing_extensions;(python_version<"3.8")and(extra=="docs")': ['0.10.0', '0.10.1', '0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0', '0.9.0a0', '0.9.0a1', '0.9.0a2', '0.9.0b0', '0.9.0b1', '0.9.1'], 'pytorch-lightning(>=1.2,<1.3)': ['0.10.1'], 'pyro-ppl(>=1.6.0)': ['0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0'], 'pytorch-lightning(>=1.3)': ['0.11.0', '0.12.0'], 'torch(>=1.8.0)': ['0.11.0', '0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0'], 'sphinx(>=3.4,<4.1);extra=="docs"': ['0.12.0'], 'sphinx_copybutton(<=0.3.1);extra=="docs"': ['0.12.0', '0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0'], 'pytorch-lightning(>=1.3,<1.4)': ['0.12.1', '0.12.2', '0.13.0', '0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6'], 'docrep(>=0.3.2)': ['0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0'], 'sphinx-panels;extra=="docs"': ['0.14.0', '0.14.1', '0.14.2', '0.14.3', '0.14.4', '0.14.5', '0.14.6', '0.15.0a0'], 'black(>=22.1);extra=="dev"': ['0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5'], 'setuptools(<=59.5.0)': ['0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1'], 'torchmetrics(>=0.6.0)': ['0.14.6', '0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0'], 'flax': ['0.15.0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'furo(>=2022.2.14.1);extra=="docs"': ['0.15.0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0'], 'jax(>=0.3)': ['0.15.0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0'], 'numpyro': ['0.15.0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0b0'], 'optax': ['0.15.0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'pymde;extra=="pymde"orextra=="tutorials"': ['0.15.0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4'], 'pynndescent;extra=="tutorials"': ['0.15.0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0'], 'pytorch-lightning(>=1.5,<1.6)': ['0.15.0', '0.15.0a0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4'], 'sphinx(>=4.1,<4.4);extra=="docs"': ['0.15.0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1'], 'sphinx-design;extra=="docs"': ['0.15.0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0'], 'sphinx_remove_toctrees;extra=="docs"': ['0.15.0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4'], 'sphinxext-opengraph;extra=="docs"': ['0.15.0', '0.15.0b0', '0.15.1', '0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0'], 'myst-parser;extra=="docs"': ['0.15.2', '0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0'], 'Jinja2(<3.1.0);extra=="docs"': ['0.15.3', '0.15.4', '0.15.5', '0.16.0', '0.16.1'], 'black(>=22.3);extra=="dev"': ['0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0'], 'importlib-metadata(>1.0);python_version<"3.8"': ['0.16.0', '0.16.1', '0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0'], 'protobuf(<=3.20.1)': ['0.16.4'], 'sphinx(>=4.1);extra=="docs"': ['0.16.4', '0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0'], 'jaxlib': ['0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0', '0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2'], 'mudata(>=0.1.2)': ['0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3', '0.17.4', '0.18.0', '0.19.0', '0.19.0a0'], 'pytorch-lightning(>=1.6.4,<1.7.0)': ['0.17.0', '0.17.0b0', '0.17.1', '0.17.2', '0.17.3'], 'sphinx-gallery(>0.6,<0.11);extra=="docs"': ['0.17.3', '0.17.4'], 'pytorch-lightning(>=1.7.0,<1.8)': ['0.17.4', '0.19.0'], 'sphinx-hoverxref;extra=="docs"': ['0.17.4', '0.18.0', '0.19.0', '0.19.0a0'], 'ml-collections(>=0.1.1)': ['0.18.0', '0.19.0', '0.19.0a0'], 'pymde;extra=="dev"orextra=="pymde"orextra=="tutorials"': ['0.18.0', '0.19.0', '0.19.0a0'], 'pytorch-lightning(>=1.6.0,<1.8)': ['0.18.0', '0.19.0a0'], 'sphinxcontrib-bibtex(>=1.0.0);extra=="docs"': ['0.18.0', '0.19.0', '0.19.0a0'], 'chex': ['0.19.0', '0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0'], 'anndata>=0.7.5': ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'docrep>=0.3.2': ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'h5py>=2.9.0': ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'jax>=0.3': ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2'], 'ml-collections>=0.1.1': ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'mudata>=0.1.2': ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'numpy>=1.17.0': ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0'], 'openpyxl>=3.0': ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3'], 'pandas>=1.0': ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.1', '1.1.2'], 'pyro-ppl>=1.6.0': ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'pytorch-lightning<1.10.0,>=1.9.0': ['0.20.0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3'], 'rich>=12.0.0': ['0.20.0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'scikit-learn>=0.21.2': ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'scipy': ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'torch>=1.8.0': ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'torchmetrics>=0.11.0': ['0.20.0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'tqdm>=4.56.0': ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "hyperopt>=0.2;extra=='autotune'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "ipython;extra=='autotune'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "ray[tune]>=2.2.0;extra=='autotune'": ['0.20.0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0'], "scib-metrics>=0.1.1;extra=='autotune'": ['0.20.0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3'], "black;extra=='dev'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "codecov;extra=='dev'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3'], "flake8;extra=='dev'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "genomepy;extra=='dev'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "isort;extra=='dev'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3'], "jupyter;extra=='dev'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "loompy>=3.0.6;extra=='dev'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "nbconvert;extra=='dev'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "nbformat;extra=='dev'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "pre-commit;extra=='dev'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "pymde;extra=='dev'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "pytest;extra=='dev'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "scanpy>=1.6;extra=='dev'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "furo;extra=='docs'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3'], "ipython;extra=='docs'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "myst-parser;extra=='docs'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "nbsphinx;extra=='docs'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3'], "sphinx-autodoc-typehints<1.21.4;extra=='docs'": ['0.20.0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1'], "sphinx-copybutton;extra=='docs'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "sphinx-design;extra=='docs'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "sphinx-hoverxref;extra=='docs'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "sphinx>=4.1;extra=='docs'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "sphinxcontrib-bibtex>=1.0.0;extra=='docs'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "sphinxext-opengraph;extra=='docs'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "huggingface-hub;extra=='hub'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "pymde;extra=='pymde'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "genomepy;extra=='tutorials'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "huggingface-hub;extra=='tutorials'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "leidenalg;extra=='tutorials'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "loompy;extra=='tutorials'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "pymde;extra=='tutorials'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "pynndescent;extra=='tutorials'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "python-igraph;extra=='tutorials'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "scanpy;extra=='tutorials'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "scikit-misc;extra=='tutorials'": ['0.20.0', '0.20.0a0', '0.20.0b0', '0.20.0b1', '0.20.0b2', '0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'pytorch-lightning<1.9.0,>=1.8.0': ['0.20.0a0', '0.20.0b0'], 'rich>=9.1.0': ['0.20.0a0', '0.20.0b0'], 'torchmetrics>=0.6.0': ['0.20.0a0', '0.20.0b0'], "ray[tune]>=2.1.0;extra=='autotune'": ['0.20.0a0'], "sphinx-autodoc-typehints;extra=='docs'": ['0.20.0a0', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'jax>=0.4.4': ['0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'jaxlib>=0.4.3': ['0.20.1', '0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "pytest-cov;extra=='dev'": ['0.20.2', '0.20.3', '1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], 'anndata(>=0.7.4)': ['0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1'], 'hyperopt(==0.1.2)': ['0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1'], 'ipython(>=7.1.1);extra=="docs"': ['0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0a0', '0.9.0a1', '0.9.0a2'], 'prospector;extra=="dev"': ['0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0a0', '0.9.0a1', '0.9.0a2'], 'pydata-sphinx-theme(>=0.4.0);extra=="docs"': ['0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0a0', '0.9.0a1'], 'rich(>=6.2.0)': ['0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0a0', '0.9.0a1', '0.9.0a2'], 'sphinx(>=3.0,<4.0);extra=="docs"': ['0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0a0', '0.9.0a1', '0.9.0a2'], 'torch(>=1.3)': ['0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0a0', '0.9.0a1', '0.9.0a2'], 'tqdm(>=4.31.1)': ['0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0', '0.8.0b0', '0.8.1', '0.9.0a0', '0.9.0a1'], 'xlrd(>=1.2.0)': ['0.7.0', '0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5', '0.7.0a6', '0.7.0b0', '0.7.1', '0.8.0b0'], 'toml': ['0.7.0a0', '0.7.0a1', '0.7.0a2', '0.7.0a3', '0.7.0a4', '0.7.0a5'], 'pyro-ppl(>=1.1.0)': ['0.9.0', '0.9.0a2', '0.9.0b0', '0.9.0b1'], 'pytorch-lightning(>1.0)': ['0.9.0a0', '0.9.0a1', '0.9.0a2'], 'sphinx-material;extra=="docs"': ['0.9.0a2'], 'furo(>=2020.12.30b24);extra=="docs"': ['0.9.0b0', '0.9.0b1'], 'lightning<2.1,>=2.0': ['1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], 'numpyro>=0.12.1': ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'sparse>=0.14.0': ['1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0rc1', '1.1.0rc2'], 'xarray>=2023.2.0': ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0rc1', '1.1.0rc2'], "scib-metrics>=0.3;extra=='autotune'": ['1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "cellxgene-census;extra=='census'": ['1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "cellxgene-census;extra=='dev'": ['1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "ruff;extra=='dev'": ['1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], "myst-nb;extra=='docs'": ['1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "sphinx-book-theme>=1.0.1;extra=='docs'": ['1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "biopython>=1.81;extra=='regseq'": ['1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "genomepy;extra=='regseq'": ['1.0.0', '1.0.0b0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'chex<=0.1.8': ['1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0rc1', '1.1.0rc2'], 'numpy>=1.21.0': ['1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "ray[tune]>=2.5.0;extra=='autotune'": ['1.0.1', '1.0.2', '1.0.3', '1.0.4'], "docutils!=0.18.*,!=0.19.*,>=0.8;extra=='docs'": ['1.0.3', '1.0.4', '1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'lightning<2.2,>=2.0': ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "scvi-tools[dev,docs,tutorials];extra=='all'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "ray[tune]<2.10.0,>=2.5.0;extra=='autotune'": ['1.1.0.post1', '1.1.0.post2', '1.1.1', '1.1.2'], "scib-metrics>=0.4.1;extra=='autotune'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "tensorboard;extra=='autotune'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "boto3;extra=='aws'": ['1.1.0.post1', '1.1.0.post2', '1.1.1', '1.1.2'], "sparse>=0.14.0;extra=='criticism'": ['1.1.0.post1', '1.1.0.post2', '1.1.1', '1.1.2'], "xarray>=2023.2.0;extra=='criticism'": ['1.1.0.post1', '1.1.0.post2', '1.1.1', '1.1.2'], "scvi-tools[editing,tests];extra=='dev'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "scvi-tools[docs,optional];extra=='docsbuild'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "jupyter;extra=='editing'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "nbformat;extra=='editing'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "pre-commit;extra=='editing'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "ruff;extra=='editing'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "loompy>=3.0.6;extra=='loompy'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "scvi-tools[autotune,aws,criticism,hub,loompy,pymde,regseq,scanpy];extra=='optional'": ['1.1.0.post1', '1.1.0.post2', '1.1.1', '1.1.2'], "scanpy>=1.6;extra=='scanpy'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "pytest;extra=='tests'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "pytest-cov;extra=='tests'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1'], "scvi-tools[optional];extra=='tests'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "cell2location;extra=='tutorials'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "gdown;extra=='tutorials'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "igraph;extra=='tutorials'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "jupyter;extra=='tutorials'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "muon;extra=='tutorials'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "plotnine;extra=='tutorials'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "pooch;extra=='tutorials'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "scrublet;extra=='tutorials'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "scvi-tools[optional];extra=='tutorials'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], "squidpy;extra=='tutorials'": ['1.1.0.post1', '1.1.0.post2', '1.1.0rc1', '1.1.0rc2', '1.1.1', '1.1.2'], 'pandas!=2.1.2,>=1.0': ['1.1.0rc1', '1.1.0rc2'], "ray[tune]<2.8.0,>=2.5.0;extra=='autotune'": ['1.1.0rc1', '1.1.0rc2'], "black;extra=='editing'": ['1.1.0rc1', '1.1.0rc2'], "flake8;extra=='editing'": ['1.1.0rc1', '1.1.0rc2'], "scvi-tools[autotune,census,hub,loompy,pymde,regseq,scanpy];extra=='optional'": ['1.1.0rc1', '1.1.0rc2'], "coverage;extra=='tests'": ['1.1.2']}
