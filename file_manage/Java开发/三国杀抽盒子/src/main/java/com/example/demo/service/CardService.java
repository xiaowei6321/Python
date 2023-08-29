package com.example.demo.service;
import org.springframework.stereotype.Service;
import java.util.Random;
@Service
public class CardService {

    public String drawCard() {
        //执行抽卡操作
//        return "抽卡成功";
        return prizeNameList[getPrize(new Random().nextInt(10000))];

    }

    //多次抽奖
    public String drawCard50() {
        //执行抽卡操作
        return printPrizeList(getPrizeList(50));
    }

    private static int[] prizeList ;
    private static String[] prizeNameList;
    private static int[] prizeCountList;
    static {

        int[] list=new int[]{500,500,1088,3000,3000,1000,250,250,250,50,50,25,25,5,5,1,1};
        prizeList = new int[]{500,1000,2088,5088,8088,9088,9338,9588,9838,9888,9938,9963,9988,9993,9998,10000};

        prizeNameList=new String[]{"史诗体验卡","欢乐豆","菜篮子","换将卡","手气卡","点将卡","进阶丹","雁翎甲","招募令","史诗宝珠碎片","菜篮子","谋庞统","史诗宝珠","将魂","霜刃绚练","史诗宝珠","谋貂蝉"};

        prizeCountList=new int[]{1,22,2,2,2,1,1,1,1,1,99,1,1,1000,1,33,1};


    }


    //单次抽奖
    public static int getPrize(int randomNum){
        int prize = 0;
        for(int i=0;i<prizeList.length;i++){
            if(randomNum<prizeList[i]){
                prize = i;
                break;
            }
        }
        return prize;
    }

    //多次抽奖
    public static int[] getPrizeList(int randomNum){
        int[] prizeList = new int[prizeNameList.length];
        for(int i=0;i<prizeNameList.length;i++){
            prizeList[i]=0;
        }
        for(int i=0;i<randomNum;i++){
            int prize = getPrize(new Random().nextInt(10000));
            prizeList[prize]++;
        }
        return prizeList;
    }

    //打印列表中不为空的奖品
    public static String printPrizeList(int[] prizeList){
        StringBuffer sb = new StringBuffer();
        for(int i=0;i<prizeList.length;i++){
            if(prizeList[i]>0){
                System.out.println(prizeNameList[i]+"："+prizeList[i]);
                sb.append(prizeNameList[i]+"："+prizeList[i]+"\n");
            }
        }
        return sb.toString();

    }

    
}
