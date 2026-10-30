import java.util.*;

public class SelfReferential {

    public static List<String> generate(String seed) {
        Set<String> seen = new LinkedHashSet<>();
        List<String> chain = new ArrayList<>();
        String current = seed;

        while (!seen.contains(current)) {
            seen.add(current);
            chain.add(current);

            Map<Character, Integer> counts = new TreeMap<>(Collections.reverseOrder());
            for (char ch : current.toCharArray()) {
                counts.merge(ch, 1, Integer::sum);
            }

            StringBuilder next = new StringBuilder();
            for (Map.Entry<Character, Integer> e : counts.entrySet()) {
                next.append(e.getValue()).append(e.getKey());
            }
            current = next.toString();
        }

        return chain;
    }

    public static void main(String[] args) {
        String seed = args.length > 0 ? args[0] : "40";
        for (String term : generate(seed)) {
            System.out.println(term);
        }
    }
}
